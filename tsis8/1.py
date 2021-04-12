import pygame, random, time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Road')
font = pygame.font.SysFont('Arial', 32)
font_over = pygame.font.SysFont('Arial', 72, bold=True, italic=True)

#images
back_image = pygame.image.load('./images/background.png')
player_image = pygame.image.load('./images/mycar.png')
enemy_image = pygame.image.load('./images/enemy.png')
heart_image = pygame.image.load('./images/heart.png')
coin_image = pygame.image.load('./images/coins.png')
coin_score_image = pygame.image.load('./images/coin_score.png')

# sounds
back_sound = pygame.mixer.Sound('./sounds/background.mp3')
back_sound.play().set_volume(0.1)

#COLORS
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

Done = False

FPS = pygame.time.Clock()

# coorinates
player_x, player_y = random.randint(150, 600), 480
enemy_x, enemy_y = random.randint(125, 630), random.randint(-500, 0)
player_dx = 5
enemy_dy = random.randint(1, 5)
coin_x = random.randint(125, 650)
coin_y = 5
coin_dy = 2

hearts = 3
coins = 0


#functions
def show_player(x, y):
    screen.blit(player_image, (x, y))
def show_enemy(x, y):
    screen.blit(enemy_image, (x, y))
def show_coin(x, y):
    screen.blit(coin_image, (x, y))
def show_coin_score(x, y):
    screen.blit(coin_score_image, (x, y))
    screen.blit(font.render(str(coins), True, White), (x + 40, y - 3))
def show_heart(x, y):
    for i in range(hearts):
        screen.blit(heart_image, (x, y))
        x += 25
def isCollision_enemy(player_x, player_y, enemy_x, enemy_y):
    if player_x in range(enemy_x-40, enemy_x + 40) and player_y in range(enemy_y - 95, enemy_y + 95):
        return True
    return False
def isCollision_coin(player_x, player_y, coin_x, coin_y):
    if player_x in range(coin_x - 40, coin_x + 25) and player_y in range(coin_y - 95, coin_y + 25):
        return True
    return False

while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Done = True

    # motion
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        player_x -= player_dx
    if pressed[pygame.K_RIGHT]:
        player_x += player_dx
    if player_x > 630:
        player_x -= player_dx
    if player_x < 125:
        player_x += player_dx

    enemy_y += enemy_dy
    if enemy_y > 640:
        enemy_y = -150
        enemy_x = random.randint(100, 600)
        enemy_dy = random.randint(1, 5)
    
    coin_y += coin_dy
    if coin_y > 630:
        coin_x = random.randint(125, 650)
        coin_y = -50

    # collisions
    isCol_coin = isCollision_coin(player_x, player_y, coin_x, coin_y)
    if isCol_coin:
        pygame.mixer.Sound('./sounds/get_coin.mp3').play()
        coin_x = random.randint(125, 650)
        coin_y = -50
        coins += 1

    isCol_enemy = isCollision_enemy(player_x, player_y, enemy_x, enemy_y)
    if isCol_enemy:
        enemy_x = random.randint(125, 630)
        enemy_y = -150
        enemy_dy = random.randint(1, 5)
        player_x = random.randint(150, 600)
        hearts -= 1
        pygame.mixer.Sound('./sounds/crash.wav').play()
        time.sleep(1)
        if hearts == 0:
            back_sound.stop()
            screen.fill(Blue)
            time.sleep(0.3)
            screen.blit(font_over.render('GAME OVER', True, Red), (180, 240))
            time.sleep(0.3)
            show_coin_score(360, 350)
            time.sleep(0.5)
            pygame.mixer.Sound('./sounds/lose.mp3').play()
            pygame.display.update()
            time.sleep(3)
            pygame.quit()

    screen.blit(back_image, (0, 0))
    show_player(player_x, player_y)
    show_enemy(enemy_x, enemy_y)
    show_coin(coin_x, coin_y)
    show_coin_score(715, 20)
    show_heart(20, 30)
    FPS.tick(90)
    pygame.display.update()

pygame.quit()