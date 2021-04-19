import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My Paint')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

back = pygame.image.load("./images/back.png")

pos_x, pos_y = None, None
prev, cur = None, None
radius = 5
color = BLACK

clock = pygame.time.Clock()
running = True

screen.blit(back, (0, 0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = RED
                radius = 5
            if event.key == pygame.K_2:
                color = GREEN
                radius = 5
            if event.key == pygame.K_3:
                color = BLUE
                radius = 5
            if event.key == pygame.K_4:
                color = BLACK
                radius = 5
            if event.key == pygame.K_e:
                color = WHITE
                radius = 10
            if event.key == pygame.K_KP_PLUS:
                radius += 5
            if event.key == pygame.K_KP_MINUS:
                radius -= 5
            if event.key == pygame.K_r:
                pygame.draw.rect(screen, color, (cur[0] - radius, cur[1] - radius, radius * 3, radius * 2))
            if event.key == pygame.K_c:
                pygame.draw.circle(screen, color, cur, radius, radius)
    if prev:
        pygame.draw.line(screen, color, prev, cur, radius)
        prev = cur

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LCTRL] and pressed[pygame.K_s]:
        name = input("Write name for the file: ")
        pygame.image.save(screen, f"{name}.png")

    if pos_x in range(370, 386) and pos_y in range(12, 28):
        color = BLACK
    if pos_x in range(392, 408) and pos_y in range(12, 28):
        color = (127, 127, 127)
    if pos_x in range(413, 429) and pos_y in range(12, 28):
        color = (136, 0, 21)
    if pos_x in range(435, 451) and pos_y in range(12, 28):
        color = (237, 28, 36)
    if pos_x in range(458, 474) and pos_y in range(12, 28):
        color = (255, 127, 39)
    if pos_x in range(479, 495) and pos_y in range(12, 28):
        color = (255, 255, 0)
    if pos_x in range(501, 517) and pos_y in range(12, 28):
        color = (34, 177, 76)
    if pos_x in range(524, 540) and pos_y in range(12, 28):
        color = (0, 162, 232)
    if pos_x in range(546, 562) and pos_y in range(12, 28):
        color = (63, 73, 204)
    if pos_x in range(567, 583) and pos_y in range(12, 28):
        color = (163, 73, 164)
    if pos_x in range(370, 386) and pos_y in range(32, 51):
        color = WHITE
    if pos_x in range(392, 408) and pos_y in range(32, 51):
        color = (195, 195, 195)
    if pos_x in range(413, 429) and pos_y in range(32, 51):
        color = (185, 122, 87)
    if pos_x in range(435, 451) and pos_y in range(32, 51):
        color = (255, 174, 201)
    if pos_x in range(458, 474) and pos_y in range(32, 51):
        color = (255, 201, 14)
    if pos_x in range(479, 495) and pos_y in range(32, 51):
        color = (239, 228, 176)
    if pos_x in range(501, 517) and pos_y in range(32, 51):
        color = (181, 230, 29)
    if pos_x in range(524, 540) and pos_y in range(32, 51):
        color = (153, 217, 234)
    if pos_x in range(546, 562) and pos_y in range(32, 51):
        color = (112, 146, 190)
    if pos_x in range(567, 583) and pos_y in range(32, 51):
        color = (200, 191, 231)
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()