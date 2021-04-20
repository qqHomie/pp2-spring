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
x_circle = False
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
            if event.key == pygame.K_q:
                chosen = BLACK
            if event.key == pygame.K_w:
                chosen = RED
            if event.key == pygame.K_e:
                chosen = GREEN
            if event.key == pygame.K_r:
                chosen = BLUE
            if event.key == pygame.K_a:
                x_rect = True
                x_circle = False
            if event.key == pygame.K_s:
                x_circle = True
                x_rect = False
            if event.key == pygame.K_ESCAPE:
                x_circle = False
                x_rect = False
            if event.key == pygame.K_d:
                chosen = WHITE
            if event.key == pygame.K_x:
                screen.fill(WHITE)
                x = 10
                for i in range(len(colors)):
                    pygame.draw.rect(screen, colors[i], (x, y, 60, 40))
                    x += 70
                screen.blit(eraser, (400, 15))
                screen.blit(rectangle, (300, 15))
                screen.blit(circ, (350, 15))
            if event.key == pygame.K_SPACE:
                pygame.image.save(screen, str(random.randint(1, 1000)) + 'qqHomie.png')
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
            if prev and prev[1] > 50 and x_rect:
                pygame.draw.rect(screen, chosen, (prev[0], prev[1], r, r))
            if prev and prev[1] > 50 + r and x_circle:
                pygame.draw.circle(screen, chosen, prev, r)
        if event.type == pygame.MOUSEMOTION: 
            cur = pygame.mouse.get_pos()
            if prev and prev[1] > 50 and not x_rect and cur[1] > 50 and not x_circle:
                pygame.draw.line(screen, chosen, prev, cur, r)
                prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
    pygame.display.flip()

    clock.tick(30)


pygame.quit()