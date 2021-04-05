import pygame
import math

pygame.init()

# window size and the name of the program
screen_width, screen_height = 800, 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sine and Cosine graphs')

# used colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# used fonts
font_1 = pygame.font.SysFont('comicsansms', 15)
font_2 = pygame.font.SysFont('arial', 20)
font_3 = pygame.font.SysFont('arial', 18)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    screen.fill(white)

    # coordinate system boundaries
    pygame.draw.rect(screen, black, (70, 10, 660, 540), 2)

    # coordinate axes
    pygame.draw.line(screen, black, (400, 10), (400, 550), 2)
    pygame.draw.line(screen, black, (70, 280), (730, 280), 2)

    # x-axis lines
    pygame.draw.line(screen, black, (70, 40), (730, 40))
    pygame.draw.line(screen, black, (70, 520), (730, 520))
    for i in range(40, 280, 60):
        pygame.draw.line(screen, black, (70, i), (730, i))
        pygame.draw.line(screen, black, (70, i + 240), (730, i + 240))
    
    # y-axis lines
    pygame.draw.line(screen, black, (100, 10), (100, 550))
    pygame.draw.line(screen, black, (700, 10), (700, 550))
    for i in range(100, 400, 100):
        pygame.draw.line(screen, black, (i, 10), (i, 550))
        pygame.draw.line(screen, black, (i + 300, 10), (i + 300, 550))
    
    # designation lines
    pygame.draw.line(screen, red, (530, 60), (570, 60))
    for i in range(530, 570, 9):
        pygame.draw.line(screen, blue, (i, 80), (i + 3, 80))
    pygame.draw.line(screen, white, (500, 41), (500, 99))

    # x-axis scalers
    for i in range(150, 700, 100):
        pygame.draw.line(screen, black, (i, 10), (i, 32))
        pygame.draw.line(screen, black, (i, 550), (i, 528))
    for i in range(125, 700, 50):
        pygame.draw.line(screen, black, (i, 10), (i, 25))
        pygame.draw.line(screen, black, (i, 535), (i, 550))
    for i in range(112, 700, 25):
        pygame.draw.line(screen, black, (i, 10), (i, 18))
        pygame.draw.line(screen, black, (i, 542), (i, 550))
    
    # y-axis scalers
    for i in range(70, 520, 60):
        pygame.draw.line(screen, black, (70, i), (85, i))
        pygame.draw.line(screen, black, (715, i), (730, i))
    for i in range(55, 520, 30):
        pygame.draw.line(screen, black, (70, i), (77, i))
        pygame.draw.line(screen, black, (723, i), (730, i))
    
    # designations
    screen.blit(font_3.render('-3', True, black), (102, 320))
    screen.blit(font_3.render('-2', True, black), (185, 320))
    screen.blit(font_3.render('-1', True, black), (260, 320))

    # sin
    for i in range(100, 700):
        sin_y1 = 240 * math.sin((i - 100) / 100 * math.pi)
        sin_y2 = 240 * math.sin((i - 99) / 100 * math.pi)
        pygame.draw.aalines(screen, red, False, [(i, 280 + sin_y1), ((i + 1), 280 + sin_y2)])
    
    # cos
    for i in range(100, 700, 2):
        cos_y1 = 240 * math.cos((i - 100) / 100 * math.pi)
        cos_y2 = 240 * math.cos((i - 99) / 100 * math.pi)
        pygame.draw.aalines(screen, blue, False, [(i, 280 + cos_y1), ((i + 1), 280 + cos_y2)])

    # designation text
    sin = font_1.render('sin x', True, black)
    screen.blit(sin, (490, 48))
    cos = font_1.render('cos x', True, black)
    screen.blit(cos, (485, 67))
    X = font_2.render('X', True, black)
    screen.blit(X, (396, 570))

    Ox = ['-3п', ' 5п', '-2п', ' 3п', '-п', ' п', ' 0', ' п', ' п', ' 3п', ' 2п', ' 5п', ' 3п']
    Oy = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0,25', '-0.50', '-0.75', '-1.00']
    fraction = ['_ __', '__', '_ _', '_']
    denominator = [' 2', '  2']

    # y-axis values
    index_Oy = 0
    Oy_coordinate = 28
    while index_Oy < len(Oy) and Oy_coordinate <= 508:
        screen.blit(font_2.render(Oy[index_Oy], True, black), (25, Oy_coordinate))
        index_Oy += 1
        Oy_coordinate += 60
    
    # x-axis values
    index_Ox = 0
    Ox_coordinate_1 = 100
    while index_Ox < len(Ox) and Ox_coordinate_1 <= 700:
        screen.blit(font_2.render(Ox[index_Ox], True, black), (Ox_coordinate_1 - 8, 548))
        index_Ox += 2
        Ox_coordinate_1 += 100
    index_Ox = 1
    Ox_coordinate_2 = 150
    while index_Ox < len(Ox) and Ox_coordinate_2 <= 700:
        screen.blit(font_2.render(Ox[index_Ox], True, black), (Ox_coordinate_2 - 10, 547))
        if Ox_coordinate_2 <= 300:
            screen.blit(font_2.render(fraction[0], True, black), (Ox_coordinate_2 - 20, 547))
            screen.blit(font_2.render(denominator[1], True, black), (Ox_coordinate_2 - 10, 566))
        if Ox_coordinate_2 == 350:
            screen.blit(font_2.render(fraction[2], True, black), (Ox_coordinate_2 - 20, 547))
            screen.blit(font_2.render(denominator[0], True, black), (Ox_coordinate_2 - 10, 566))
        if Ox_coordinate_2 == 450:
            screen.blit(font_2.render(fraction[3], True, black), (Ox_coordinate_2 - 6, 547))
            screen.blit(font_2.render(denominator[0], True, black), (Ox_coordinate_2 - 10, 566))
        if Ox_coordinate_2 > 500:
            screen.blit(font_2.render(fraction[1], True, black), (Ox_coordinate_2 - 5, 547))
            screen.blit(font_2.render(denominator[1], True, black), (Ox_coordinate_2 - 10, 566))
        index_Ox += 2
        Ox_coordinate_2 += 100
    
    pygame.display.flip()

pygame.quit()