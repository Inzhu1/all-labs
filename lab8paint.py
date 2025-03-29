import pygame


pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLUE

radius = 5
mode = "pen" 
start_pos = None
is_drawing = False
points = []


screen.fill(BLACK)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_t:
                mode = "rect"
            elif event.key == pygame.K_EQUALS:
                radius = min(50, radius + 1)
            elif event.key == pygame.K_MINUS:
                radius = max(1, radius - 1)
            elif event.key == pygame.K_ESCAPE:
                screen.fill(BLACK)
                pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            is_drawing = True
            if mode == "pen":
                points.append(event.pos)
        
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            is_drawing = False
            if mode == "rect":
                rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                   abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)
            elif mode == "circle":
                center = start_pos
                radius = int(((end_pos[0] - start_pos[0])  2 + (end_pos[1] - start_pos[1])  2) ** 0.5)
                pygame.draw.circle(screen, current_color, center, radius, 2)
            pygame.display.flip()

        if event.type == pygame.MOUSEMOTION and is_drawing:
            if mode == "pen":
                pygame.draw.line(screen, current_color, points[-1], event.pos, radius)
                points.append(event.pos)
            elif mode == "eraser":
                pygame.draw.circle(screen, BLACK, event.pos, radius)
            pygame.display.flip()

    clock.tick(60)

pygame.quit()
