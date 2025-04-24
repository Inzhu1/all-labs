import pygame
import random
import time
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="Snake",
    user="inzhuaitakhyn",
    password="inzhu2007",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Создание таблиц, если их нет
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_scores (
    user_id INTEGER REFERENCES users(id),
    score INTEGER NOT NULL,
    level INTEGER NOT NULL,
    PRIMARY KEY (user_id)
);
""")
conn.commit()

# Pygame настройки
pygame.init()
WIDTH, HEIGHT, CELL = 600, 600, 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont(None, 36)

# Цвета
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        self.body[0].x = (self.body[0].x + self.dx) % (WIDTH // CELL)
        self.body[0].y = (self.body[0].y + self.dy) % (HEIGHT // CELL)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, WHITE, (segment.x * CELL, segment.y * CELL, CELL, CELL))

class Food:
    def __init__(self):
        self.generate()

    def generate(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        self.color = RED if random.random() < 0.2 else GREEN
        self.weight = 3 if self.color == RED else 2
        self.time_created = time.time()

    def update(self):
        if time.time() - self.time_created > 7:
            self.generate()

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

class Wall:
    def __init__(self, level):
        self.body = []
        self.generate(level)

    def generate(self, level):
        self.body.clear()
        if level >= 2:
            for i in range(5, 15):
                self.body.append(Point(i, 10))
        if level >= 4:
            for i in range(5, 15):
                self.body.append(Point(10, i))

    def draw(self):
        for w in self.body:
            pygame.draw.rect(screen, GRAY, (w.x * CELL, w.y * CELL, CELL, CELL))

def get_or_create_user(username):
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result:
        user_id = result[0]
    else:
        cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cursor.fetchone()[0]
        conn.commit()
    return user_id

def get_user_stats(user_id):
    cursor.execute("SELECT score, level FROM user_scores WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    if result:
        return result[0], result[1]
    else:
        cursor.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, 0, 1))
        conn.commit()
        return 0, 1

def save_user_stats(user_id, score, level):
    cursor.execute("""
        INSERT INTO user_scores (user_id, score, level)
        VALUES (%s, %s, %s)
        ON CONFLICT (user_id) DO UPDATE 
        SET score = GREATEST(user_scores.score, %s), level = %s
    """, (user_id, score, level, score, level))
    conn.commit()

def username_input_screen():
    username = ""
    input_active = True
    while input_active:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username:
                    return username
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
        label = font.render("Enter Username: " + username, True, WHITE)
        screen.blit(label, (WIDTH // 4, HEIGHT // 2))
        pygame.display.flip()

def welcome_screen(username, score, level):
    waiting = True
    while waiting:
        screen.fill(BLACK)
        t1 = font.render(f"Welcome, {username}!", True, WHITE)
        t2 = font.render(f"Score: {score} | Level: {level}", True, WHITE)
        t3 = font.render("Press SPACE to start", True, GREEN)
        screen.blit(t1, (WIDTH // 4, HEIGHT // 3))
        screen.blit(t2, (WIDTH // 4, HEIGHT // 3 + 40))
        screen.blit(t3, (WIDTH // 4, HEIGHT // 3 + 100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

def draw_score(score, level):
    label = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(label, (10, 10))

def draw_button(text, x, y, w, h):
    pygame.draw.rect(screen, GRAY, (x, y, w, h))
    label = font.render(text, True, BLACK)
    screen.blit(label, (x + 10, y + 10))

# --- Main Game ---

username = username_input_screen()
user_id = get_or_create_user(username)
score, level = get_user_stats(user_id)
welcome_screen(username, score, level)

FPS = 5 + level
clock = pygame.time.Clock()
snake = Snake()
food = Food()
wall = Wall(level)
paused = False
running = True

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_user_stats(user_id, score, level)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1
            elif event.key == pygame.K_p:
                paused = not paused
                save_user_stats(user_id, score, level)

    if not paused:
        snake.move()
        if snake.body[0].x == food.pos.x and snake.body[0].y == food.pos.y:
            score += food.weight
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
            food.generate()
            if score % 5 == 0:
                level += 1
                FPS = 5 + level
                wall = Wall(level)
        for w in wall.body:
            if snake.body[0].x == w.x and snake.body[0].y == w.y:
                save_user_stats(user_id, score, level)
                print("Game over — collided with wall!")
                pygame.quit()
                exit()
        food.update()

    wall.draw()
    snake.draw()
    food.draw()
    draw_score(score, level)
    draw_button("Pause", WIDTH - 120, 10, 100, 40)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
