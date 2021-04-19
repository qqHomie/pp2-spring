import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = [BLACK, RED, GREEN, BLUE]
chosen = WHITE
x = 10
y = 10
x_rect = False
r = 10

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

eraser = pygame.image.load('./images/eraser.png')
rectangle = pygame.image.load('./images/rect.png')
circ = pygame.image.load('./images/circle.png')
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

game_over = False

prev, cur = None, None
screen.fill(WHITE)

for i in range(len(colors)):
    pygame.draw.rect(screen, colors[i], (x, y, 60, 40))
    x += 70
screen.blit(eraser, (400, 15))
screen.blit(rectangle, (300, 15))
screen.blit(circ, (350, 15))

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                r += 1
            if event.key == pygame.K_DOWN:
                r -= 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
            if prev[0] in range(10, 70) and prev[1] in range(10, 50):
                chosen = BLACK
                x_rect = False
            if prev[0] in range(80, 140) and prev[1] in range(10, 50):
                chosen = RED
                x_rect = False
            if prev[0] in range(150, 210) and prev[1] in range(10, 50):
                chosen = GREEN
                x_rect = False
            if prev[0] in range(220, 280) and prev[1] in range(10, 50):
                chosen = BLUE
                x_rect = False
            if prev[0] in range(400, 432) and prev[1] in range(15, 47):
                chosen = WHITE
                x_rect = False
            if prev[0] in range(300, 332) and prev[1] in range(15, 47):
                x_rect = True
        if event.type == pygame.MOUSEMOTION: 
            cur = pygame.mouse.get_pos()
            if prev and prev[1] > 50 and not x_rect and cur[1] > 50:
                pygame.draw.line(screen, chosen, prev, cur, r)
                prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
    pygame.display.flip()

    clock.tick(30)


pygame.quit()