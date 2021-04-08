import pygame
from math import pi, sin, cos

pygame.init()

screen = pygame.display.set_mode((800, 600))
isDone = False
font = pygame.font.SysFont("Arial", 18, italic=True)
font1 = pygame.font.SysFont("Arial", 26)

y_number = ['1.00', '0.75', '0.50', '0.25', '0.00', '0.25', '0.50', '0.75', '1.00']
x_number = ['3п', '2п', 'п', '0', 'п', '2п', '3п']
minus = ['-', '-', '-']
minus_y = ['-', '-', '-', '-']
numerators_left = ['5п', '3п', 'п']
numerators_right = ['п', '3п', '5п']
denumerators_left = ['2', '2', '2']
denumerators_right = ['2', '2', '2']
underline = ['__', '__', '_']
underlineR = ['_', '__', '__']

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0 , 255)

maxi = 400
mini = 400

while not isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                isDone = True
    
    screen.fill(white)



    for x in range(100, 700):
        sin_y1 = 240 * sin((x - 100) / 100 * pi)
        sin_y2 = 240 * sin((x - 99) / 100 * pi)
        maxi = max(maxi, sin_y1+280, sin_y2+280)
        mini = min(mini, sin_y1+280, sin_y2+280)
        pygame.draw.aalines(screen, red, True, [(x, 280 + sin_y1), ((x + 1), 280 + sin_y2)], 30)
    
    for x in range(100, 700, 2):
        cos_y1 = 240 * cos((x - 100) / 100 * pi)
        cos_y2 = 240 * cos((x - 99) / 100 * pi)
        pygame.draw.aalines(screen, blue, True, [(x, 280 + cos_y1), ((x + 1), 280 + cos_y2)])

    for x in range(100, 800, 100):
        pygame.draw.line(screen, black, (x, mini-25), (x, maxi+25))
    
    for y in range(int(mini), int(maxi)+(int((maxi-mini)//8)), int((maxi-mini)//8)):
        pygame.draw.line(screen, black, (75, y), (725, y))
    
    for x in range(75, 726, 325):
        pygame.draw.line(screen, black, (x, mini-25), (x, maxi+25), 2)
    
    for y in range(int(mini-25), int(maxi+25)+1, int((maxi-mini+50)/2)):
        pygame.draw.line(screen, black, (75, y), (725, y), 2)


    # x-measures
    for x in range(150, 701, 50):
        pygame.draw.line(screen, black, (x, int(mini-25)), (x, int(mini-7)))
    for x in range(150, 701, 50):
        pygame.draw.line(screen, black, (x, int(maxi+7)), (x, int(maxi+25)))
    for x in range(125, 701, 25):
        pygame.draw.line(screen, black, (x, int(mini-25)), (x, int(mini-15)))
    for x in range(125, 701, 25):
        pygame.draw.line(screen, black, (x, int(maxi+15)), (x, int(maxi+25)))
    for x in range(112, 701, 25):
        pygame.draw.line(screen, black, (x, int(mini-25)), (x, int(mini-20)))
    for x in range(112, 701, 25):
        pygame.draw.line(screen, black, (x, int(maxi+20)), (x, int(maxi+25)))


    
    # y-measures
    for y in range(int(mini+(((maxi-mini)//8)//2)), int(maxi), int((maxi-mini)//8)):
        pygame.draw.line(screen, black, (75, y), (88, y))
    for y in range(int(mini+(((maxi-mini)//8)//2)), int(maxi), int((maxi-mini)//8)):
        pygame.draw.line(screen, black, (712, y), (725, y))
    for y in range(int(mini+(((maxi-mini)//8)//4)), int(maxi), int((maxi-mini)//16)):
        pygame.draw.line(screen, black, (75, y), (80, y))
    for y in range(int(mini+(((maxi-mini)//8)//4)), int(maxi), int((maxi-mini)//16)):
        pygame.draw.line(screen, black, (720, y), (725, y))

    
    # y axis measures
    y_coor = mini
    for i in range(len(y_number)):
        screen.blit(font.render(str(y_number[i]), True, black), (25, int(y_coor)-10))
        y_coor += 60
        

    # x axis measures
    x_coor = 100
    for i in range(len(x_number)):
        screen.blit(font.render(str(x_number[i]), True, black), (x_coor-3, int(maxi+25)))
        x_coor += 100


    # char minus
    char_coor = 100
    for i in range(len(minus)):
        screen.blit(font.render(str(minus[i]), True, black), (char_coor-10, int(maxi+25)))
        char_coor += 100
    y_char = maxi
    for i in range(len(minus_y)):
        screen.blit(font.render(str(minus_y[i]), True, black), (15, int(y_char)-12))
        y_char -= 60


    # fractions left
    frac_coor = 150
    for i in range(len(numerators_left)):
        screen.blit(font.render(str(numerators_left[i]), True, black), (frac_coor-6, int(maxi+23)))
        screen.blit(font.render(str(underline[i]), True, black), (frac_coor-7, int(maxi+23)))
        screen.blit(font.render(str(minus[i]), True, black), (frac_coor-14, int(maxi+30)))
        frac_coor += 100
    denom_coor = 150
    for i in range(2):
        screen.blit(font.render('2', True, black), (denom_coor-3, int(maxi+43)))
        denom_coor += 100
    screen.blit(font.render('2', True, black), (denom_coor-6, int(maxi+43)))

    # fractiions right
    frac_coorR = 450
    for i in range(len(numerators_right)):
        screen.blit(font.render(str(numerators_right[i]), True, black), (frac_coorR-5, int(maxi+23)))
        screen.blit(font.render(str(underlineR[i]), True, black), (frac_coorR-6, int(maxi+23)))
        frac_coorR += 100
    denom_coorR = 550
    for i in range(2):
        screen.blit(font.render('2', True, black), (denom_coorR-2, int(maxi+43)))
        denom_coorR += 100
    screen.blit(font.render('2', True, black), (denom_coorR-306, int(maxi+43)))

    # sin and cos lines color
    pygame.draw.line(screen, white, (500, int(mini+1)), (500, int(mini+59)), 3)
    screen.blit(font1.render('sin x', True, black), (487, int(mini+1)))
    screen.blit(font1.render('cos x', True, black), (481, int(mini+27)))
    pygame.draw.line(screen, red, (537, int(mini+20)), (572, int(mini+20)))
    for x in range(537, 572, 13):
        pygame.draw.line(screen, blue, (x, int(mini+46)), (x+7, int(mini+46)))

    pygame.display.update()
pygame.quit()