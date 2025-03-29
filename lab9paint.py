import pygame
import math

# Initialize pygame
pygame.init()

# Set up screen dimensions and clock
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLUE  # Default color

# Brush size and drawing mode
radius = 5
mode = "pen"  # Default mode
start_pos = None
is_drawing = False
points = []

# Fill screen with black at the start
screen.fill(BLACK)
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle key presses for changing tools and colors
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
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_y:
                mode = "right_triangle"
            elif event.key == pygame.K_q:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
            elif event.key == pygame.K_EQUALS:
                radius = min(50, radius + 1)
            elif event.key == pygame.K_MINUS:
                radius = max(1, radius - 1)
            elif event.key == pygame.K_ESCAPE:
                screen.fill(BLACK)
                pygame.display.flip()

        # Handle mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            is_drawing = True
            if mode == "pen":
                points.append(event.pos)
        
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            is_drawing = False
            if mode == "rect":
                # Draw a rectangle
                rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                   abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)
            elif mode == "circle":
                # Draw a circle
                center = start_pos
                radius = int(math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2))
                pygame.draw.circle(screen, current_color, center, radius, 2)
            elif mode == "square":
                # Draw a square
                side_length = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                rect = pygame.Rect(start_pos[0], start_pos[1], side_length, side_length)
                pygame.draw.rect(screen, current_color, rect, 2)
            elif mode == "right_triangle":
                # Draw a right triangle
                pygame.draw.polygon(screen, current_color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
            elif mode == "equilateral_triangle":
                # Draw an equilateral triangle
                side_length = abs(end_pos[0] - start_pos[0])
                height = (math.sqrt(3) / 2) * side_length
                pygame.draw.polygon(screen, current_color, [
                    start_pos,
                    (start_pos[0] + side_length, start_pos[1]),
                    (start_pos[0] + side_length / 2, start_pos[1] - height)
                ], 2)
            elif mode == "rhombus":
                # Draw a rhombus (diamond shape)
                dx = abs(end_pos[0] - start_pos[0]) // 2
                dy = abs(end_pos[1] - start_pos[1]) // 2
                center_x, center_y = start_pos
                pygame.draw.polygon(screen, current_color, [
                    (center_x, center_y - dy),
                    (center_x + dx, center_y),
                    (center_x, center_y + dy),
                    (center_x - dx, center_y)
                ], 2)
            pygame.display.flip()

        if event.type == pygame.MOUSEMOTION and is_drawing:
            # Drawing with pen or eraser
            if mode == "pen":
                pygame.draw.line(screen, current_color, points[-1], event.pos, radius)
                points.append(event.pos)
            elif mode == "eraser":
                pygame.draw.circle(screen, BLACK, event.pos, radius)
            pygame.display.flip()

    clock.tick(60)

pygame.quit()
