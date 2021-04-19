import pygame, random, time

pygame.init()

WIDTH = 480
HEIGHT = 480

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (238, 236, 8)

FPS = pygame.time.Clock()
fps = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Snake Game')
font = pygame.font.SysFont('Arial', 30, bold=True)
font1 = pygame.font.SysFont('Arial', 30, bold=True, italic=True)
font_score = pygame.font.SysFont('Arial', 18, bold=True)
back_image = pygame.image.load('./images/background.png')
first_image = pygame.image.load('./images/first.png')
second_image = pygame.image.load('./images/second.png')

pygame.mixer.music.load('./sounds/menu.mp3')
game_music = pygame.mixer.Sound('./sounds/game.mp3')
eat_music = pygame.mixer.Sound('./sounds/eaten.mp3')

Done = False
easy = False
medium = False
hard = False
multi_players = False
menu = True
level = True

snake1_here = True
snake2_here = True


class Snake:

    def __init__(self, x, y):
        self.size = 1
        self.dx = 0
        self.dy = 0
        self.elements = [[x, y]]
        self.score = 0
        self.is_add = False
        self.fps = 30

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, (101, 209, 209), (element[0], element[1], 18, 18))

    def draw_second(self):
        for element in self.elements:
            pygame.draw.rect(screen, (243, 242, 65), (element[0], element[1], 18, 18))
    
    
    def move(self):
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
        

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
            
        if self.is_add:
            self.add_snake()

    def add_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([-20, -20])
        self.is_add = False
    

class Food:

    def __init__(self):
        self.x = random.randrange(40, WIDTH - 40, 20)
        self.y = random.randrange(40, HEIGHT - 40, 20)
        self.image = pygame.image.load('./images/apple.png')
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    
def show_score(x, y, score):
    screen.blit(font_score.render('Score: ' + str(score), True, WHITE), (x, y))


def show_walls():
    wall_images = pygame.image.load('./images/wall.png')
    for i in range(0, WIDTH, 30):
        screen.blit(wall_images, (i, 0))
        screen.blit(wall_images, (0, i))
        screen.blit(wall_images, (i, HEIGHT - 30))
        screen.blit(wall_images, (WIDTH - 30, i))
    for i in range(38, 443, 404):
        pygame.draw.line(screen, BLACK, (38, i), (442, i))
        pygame.draw.line(screen, BLACK, (i, 38), (i, 442))

def extra_walls():
    pygame.draw.rect(screen, RED, (121, 121, 98, 38))
    pygame.draw.rect(screen, (148, 65, 255), (480-121-98, 480-121-38, 98, 38))
    pygame.draw.rect(screen, YELLOW, (480-121-38, 121, 38, 98))
    pygame.draw.rect(screen, BLUE, (121, 480-121-98, 38, 98))
    pygame.draw.rect(screen, GREEN, (221, 221, 38, 38))
    for i in range(121, 221, 98):
        pygame.draw.line(screen, BLACK, (i, 121), (i, 159))
    for i in range(121, 160, 38):
        pygame.draw.line(screen, BLACK, (121, i), (219, i))
    for i in range(321, 360, 38):
        pygame.draw.line(screen, BLACK, (i, 121), (i, 219))
    for i in range(121, 221, 98):
        pygame.draw.line(screen, BLACK, (321, i), (359, i))
    for i in range(261, 361, 98):
        pygame.draw.line(screen, BLACK, (121, i), (159, i))
    for i in range(121, 161, 38):
        pygame.draw.line(screen, BLACK, (i, 261), (i, 359))
    for i in range(261, 361, 98):
        pygame.draw.line(screen, BLACK, (i, 321), (i, 359))
    for i in range(321, 361, 38):
        pygame.draw.line(screen, BLACK, (261, i), (359, i))
    for i in range(221, 261, 38):
        pygame.draw.line(screen, BLACK, (i, 221), (i, 259))
        pygame.draw.line(screen, BLACK, (221, i), (259, i))

def in_walls():
    return snake.elements[0][0] >= 435 or snake.elements[0][0] < 35 or snake.elements[0][1] >= 435 or snake.elements[0][1] < 35

def hard_in_walls():
    if ((110 <= snake.elements[0][0] < 215) and (110 <= snake.elements[0][1] < 155)):
        return True
    if ((310 <= snake.elements[0][0] < 355) and (110 <= snake.elements[0][1] < 215)):
        return True
    if ((110 <= snake.elements[0][0] < 155) and (250 <= snake.elements[0][1] < 355)):
        return True
    if ((250 <= snake.elements[0][0] < 355) and (310 <= snake.elements[0][1] < 355)):
        return True
    if ((210 <= snake.elements[0][0] < 255) and (210 <= snake.elements[0][1] < 255)):
        return True
    else:
        return False

def in_walls_2():
    if snake2.elements[0][0] >= 435 or snake2.elements[0][0] < 35 or snake2.elements[0][1] >= 435 or snake2.elements[0][1] < 35:
            return True
    return False

def in_snake():
    if len(snake.elements) > 10:
        for i in range(len(snake.elements) - 1, 8, -1):
            if snake.elements[i][0] in range(snake.elements[0][0] - 15, snake.elements[0][0] + 15) and snake.elements[i][1] in range(snake.elements[0][1] - 15, snake.elements[0][1] + 15):
                return True
    if multi_players:            
        for i in range(snake2.size):
            if snake.elements[0][0] in range(snake2.elements[i][0] - 15, snake2.elements[i][0] + 15) and snake.elements[0][1] in range(snake2.elements[i][1] - 15, snake2.elements[i][1] + 15):
                return True
    return False

def in_snake_second():
    if len(snake2.elements) > 10:
        for i in range(len(snake2.elements) - 1, 8, -1):
            if snake2.elements[i][0] in range(snake2.elements[0][0] - 15, snake2.elements[0][0] + 15) and snake2.elements[i][1] in range(snake2.elements[0][1] - 15, snake2.elements[0][1] + 15):
                return True
    for i in range(snake.size):
        if snake2.elements[0][0] in range(snake.elements[i][0] - 15, snake.elements[i][0] + 15) and snake2.elements[0][1] in range(snake.elements[i][1] - 15, snake.elements[i][1] + 15):
            return True
    return False

def collision():
    if (snake.elements[0][0] in range(food.x - 15, food.x + 20)) and (snake.elements[0][1] in range(food.y - 15, food.y + 20)):
        eat_music.play()
        snake.is_add = True
        new_x = random.randrange(40, WIDTH - 40, 20)
        new_y = random.randrange(40, HEIGHT - 40, 20)
        for i in range(len(snake.elements)):
            if (new_x == snake.elements[i][0]):
                while True:
                    new_x = random.randrange(40, WIDTH - 40, 20)
                    if new_x != snake.elements[i][0]:
                        break
            if (new_y == snake.elements[i][1]):
                while True:
                    new_y = random.randrange(40, HEIGHT - 40, 20)
                    if new_y != snake.elements[i][1]:
                        break
        if new_x in range(120, 220) and new_y in range(120, 160) and hard == True:
            while True:
                new_x = random.randrange(40, 440, 20)
                if new_x not in range(120, 220):
                    break
        if new_x in range(320, 360) and new_y in range(120, 220) and hard == True:
            while True:
                new_x = random.randrange(40, 440, 20)
                if new_x not in range(320, 360):
                    break
        if new_x in range(120, 160) and new_y in range(260, 360) and hard == True:
            while True:
                new_x = random.randrange(40, 440, 20)
                if new_x not in range(120, 160):
                    break
        if new_x in range(260, 360) and new_y in range(320, 360) and hard == True:
            while True:
                new_x = random.randrange(40, 440, 20)
                if new_x not in range(260, 360):
                    break
        if new_x in range(220, 260) and new_y in range(220, 260) and hard == True:
            while True:
                new_x = random.randrange(40, 440, 20)
                if new_x not in range(220, 260):
                    break
        food.x = new_x
        food.y = new_y
    
def collision_2():
    if(snake2.elements[0][0] in range(food.x - 15, food.x + 20)) and (snake2.elements[0][1] in range(food.y - 15, food.y + 20)):
        eat_music.play()
        snake2.is_add = True
        new_x2 = random.randrange(40, WIDTH - 40, 20)
        new_y2 = random.randrange(40, HEIGHT - 40, 20)
        for i in range(len(snake2.elements)):
            if (new_x2 == snake2.elements[i][0]):
                while True:
                    new_x2 = random.randrange(40, WIDTH - 40, 20)
                    if new_x2 != snake2.elements[i][0]:
                        break
            if (new_y2 == snake2.elements[i][1]):
                while True:
                    new_y2 = random.randrange(40, HEIGHT - 40, 20)
                    if new_y2 != snake2.elements[i][1]:
                        break
        food.x = new_x2
        food.y = new_y2

def menu():
    snake_image = pygame.image.load('./images/snake.png')
    welcome_image = pygame.image.load('./images/welcome.png')

    screen.fill((221, 163, 8)) 
    screen.blit(welcome_image, (70, 20))
    screen.blit(snake_image, (180, 100))
    pygame.draw.rect(screen, GREEN, (120, 240, 240, 50))
    pygame.draw.rect(screen, YELLOW, (120, 300, 240, 50))
    pygame.draw.rect(screen, RED, (120, 360, 240, 50))
    pygame.draw.rect(screen, BLUE, (120, 420, 240, 50))
    screen.blit(font.render('Easy', True, (BLACK)), (206, 246))
    screen.blit(font.render('Medium', True, (BLACK)), (185, 306))
    screen.blit(font.render('Hard', True, (BLACK)), (206, 366))
    screen.blit(font.render('2 players', True, (BLACK)), (175, 426))
    for i in range(240, 300, 50):
        pygame.draw.line(screen, BLACK, (120, i), (360, i), 2)
    for i in range(300, 360, 50):
        pygame.draw.line(screen, BLACK, (120, i), (360, i), 2)
    for i in range(360, 420, 50):
        pygame.draw.line(screen, BLACK, (120, i), (360, i), 2)
    for i in range(420, 480, 50):
        pygame.draw.line(screen, BLACK, (120, i), (360, i), 2)
    for i in range(120, 370, 240):
        pygame.draw.line(screen, BLACK, (i, 240), (i, 290), 2)
    for i in range(120, 370, 240):
        pygame.draw.line(screen, BLACK, (i, 300), (i, 350), 2)
    for i in range(120, 370, 240):
        pygame.draw.line(screen, BLACK, (i, 360), (i, 410), 2)
    for i in range(120, 370, 240):
        pygame.draw.line(screen, BLACK, (i, 420), (i, 470), 2)
    
def game_over():
    over_image = pygame.image.load('./images/game_over.png')
    screen.fill((80, 65, 75))
    screen.blit(over_image, (120, 20))
    screen.blit(first_image, (200, 300))
    screen.blit(font_score.render(': ' + str(snake.score), True, WHITE), (240, 305))
    pygame.display.update()
    time.sleep(2)

def game_over_multi():
    over_image = pygame.image.load('./images/game_over.png')
    screen.fill((80, 65, 75))
    screen.blit(over_image, (120, 20))
    screen.blit(first_image, (50, 300))
    screen.blit(second_image, (390, 300))
    screen.blit(font_score.render(': ' + str(snake.score), True, WHITE), (90, 305))
    screen.blit(font_score.render(': ' + str(snake2.score), True, WHITE), (430, 305))
    pygame.display.update()
    time.sleep(2)

snake = Snake(140, 100)
snake2 = Snake(340, 380)
food = Food()

speed = 5

game_music.play(-1).set_volume(0.5)

while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and snake.dx != -speed:
                snake.dx = speed
                snake.dy = 0
            if event.key == pygame.K_a and snake.dx != speed:
                snake.dx = -speed
                snake.dy = 0
            if event.key == pygame.K_w and snake.dy != speed:
                snake.dx = 0
                snake.dy = -speed
            if event.key == pygame.K_s and snake.dy != -speed:
                snake.dx = 0
                snake.dy = speed
            if event.key == pygame.K_RIGHT and snake2.dx != -speed:
                snake2.dx = speed
                snake2.dy = 0
            if event.key == pygame.K_LEFT and snake2.dx != speed:
                snake2.dx = -speed
                snake2.dy = 0
            if event.key == pygame.K_UP and snake2.dy != speed:
                snake2.dx = 0
                snake2.dy = -speed
            if event.key == pygame.K_DOWN and snake2.dy != -speed:
                snake2.dx = 0
                snake2.dy = speed
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if mouse[0] in range(120, 360) and mouse[1] in range(240, 290) and level:
                easy = True
                level = False
                medium = False
                hard = False
                multi_players = False
                menu = False
            if mouse[0] in range(120, 360) and mouse[1] in range(300, 350) and level:
                easy = False
                level = False
                medium = True
                hard = False
                multi_players = False
                menu = False
            if mouse[0] in range(120, 360) and mouse[1] in range(360, 410) and level:
                easy = False
                level = False
                medium = False
                hard = True
                multi_players = False
                menu = False
            if mouse[0] in range(120, 360) and mouse[1] in range(420, 470) and level:
                easy = False
                level = False
                medium = False
                hard = False
                multi_players = True
                menu = False

    if menu:
        menu()
    pressed = pygame.key.get_pressed()
    if easy:
        screen.blit(back_image, (0, 0))
        snake.draw()
        food.draw()
        snake.move()
        collision()
        show_score(5, 5, snake.score)
        if snake.elements[0][0] > 480:
            snake.elements[0][0] = snake.elements[0][0] % 500
        if snake.elements[0][0] < 0:
            snake.elements[0][0] = snake.elements[0][0] % 480
        if snake.elements[0][1] > 480:
            snake.elements[0][1] = snake.elements[0][1] % 500
        if snake.elements[0][1] < 0:
            snake.elements[0][1] = snake.elements[0][1] % 480
        if in_snake():
            with open('easy.txt', 'a') as f:
                f.write(str(snake.score) + '\n')
            time.sleep(1.2)
            game_over()
            Done = True
    if medium:
        snake.fps = 50
        screen.blit(back_image, (0, 0))
        snake.draw()
        food.draw()
        snake.move()
        collision()
        show_walls()
        show_score(5, 5, snake.score)
        if in_walls() or in_snake():
            with open('medium.txt', 'a') as f:
                f.write(str(snake.score) + '\n')
            time.sleep(1.2)
            game_over()
            Done = True
    if hard:
        snake.fps = 40
        screen.blit(back_image, (0, 0))
        snake.draw()
        food.draw()
        snake.move()
        collision()
        show_walls()
        extra_walls()
        show_score(5, 5, snake.score)
        if in_walls() or in_snake() or hard_in_walls():
            print(snake.elements[0])
            with open('hard.txt', 'a') as f:
                f.write(str(snake.score) + '\n')
            time.sleep(1.2)
            game_over()
            Done = True
    if multi_players:
        screen.blit(back_image, (0, 0))
        if snake1_here:
            snake.draw()
            snake.move()
            collision()
        if snake2_here:
            snake2.draw_second()
            snake2.move()
            collision_2()
        food.draw()
        show_walls()
        show_score(5, 5, snake.score)
        show_score(400, 5, snake2.score)
        if in_walls() or in_snake():
            snake1_here = False
        if in_walls_2() or in_snake_second():
            snake2_here = False
        if not snake1_here and not snake2_here:
            game_over_multi()
            Done = True

    FPS.tick(snake.fps)
    pygame.display.update()


pygame.quit()