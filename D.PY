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

# History stacks
undo_stack = []
redo_stack = []

# Main loop
drawing = False
clock = pygame.time.Clock()

def draw_circle(pos):
    pygame.draw.circle(screen, current_color, pos, brush_size)

def save_state():
    undo_stack.append(screen.copy())
    if len(undo_stack) > 50:  # Limit history size
        undo_stack.pop(0)

def undo():
    if undo_stack:
        redo_stack.append(screen.copy())
        screen.blit(undo_stack.pop(), (0, 0))

def redo():
    if redo_stack:
        undo_stack.append(screen.copy())
        screen.blit(redo_stack.pop(), (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            save_state()
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
                current_color = BLACK
            elif event.key == pygame.K_2:
                tool = "brush"
                brush_size = 10
                current_color = BLACK
            elif event.key == pygame.K_e:
                tool = "eraser"
                current_color = WHITE
            elif event.key == pygame.K_c:
                save_state()
                screen.fill(WHITE)
            elif event.key == pygame.K_r:
                current_color = (255, 0, 0)
            elif event.key == pygame.K_g:
                current_color = (0, 255, 0)
            elif event.key == pygame.K_b:
                current_color = (0, 0, 255)
            elif event.key == pygame.K_k:
                current_color = BLACK
            elif event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                undo()
            elif event.key == pygame.K_y and pygame.key.get_mods() & pygame.KMOD_CTRL:
                redo()

    pygame.display.update()
    clock.tick(60)