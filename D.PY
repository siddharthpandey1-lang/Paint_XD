import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Painting App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
current_color = BLACK

# Brush settings
brush_size = 5
tool = "pencil"

# Fill background
screen.fill(WHITE)

# Main loop
drawing = False
clock = pygame.time.Clock()

def draw_circle(pos):
    pygame.draw.circle(screen, current_color, pos, brush_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            draw_circle(event.pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        elif event.type == pygame.MOUSEMOTION and drawing:
            draw_circle(event.pos)

        # Keyboard controls
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = "pencil"
                brush_size = 3
            elif event.key == pygame.K_2:
                tool = "brush"
                brush_size = 10
            elif event.key == pygame.K_c:
                screen.fill(WHITE)
            elif event.key == pygame.K_r:
                current_color = (255, 0, 0)
            elif event.key == pygame.K_g:
                current_color = (0, 255, 0)
            elif event.key == pygame.K_b:
                current_color = (0, 0, 255)
            elif event.key == pygame.K_k:
                current_color = BLACK

    pygame.display.update()
    clock.tick(60)