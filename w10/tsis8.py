import pygame
import random
import time

pygame.init()

screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Street racing')

grass = pygame.image.load("./images/grass.png")
my_car = pygame.image.load("./images/BMW.png")
oncoming = pygame.image.load("./images/police.png")
coin_corner = pygame.image.load("./images/сoin_corner.png")
coin = pygame.image.load("./images/coin.png")
heart = pygame.image.load("./images/heart.png")
gameover = pygame.image.load("./images/gameover.png")

font = pygame.font.SysFont("times-new-roman", 50)

background_sound = pygame.mixer.Sound("./sounds/background.wav")
background_sound.play(-1)

white = (255, 255, 255)
dark_gray = (128, 128, 128)
gray = (180, 180, 180)
yellow = (255, 255, 0)

mycar_x = 270
mycar_y = 450
mycar_dx = 5

oncoming_x = random.randint(75, 465)
oncoming_y = -150
oncoming_dy = random.randint(1, 5)

coin_x = random.randint(75, 475)
coin_y = -50
coin_dy = 1

score = 0
hearts = 3

def construct_background():
    screen.blit(grass, (0, 0))
    pygame.draw.rect(screen, gray, (40, 0, 520, 600))
    pygame.draw.rect(screen, dark_gray, (40, 0, 15, 600))
    pygame.draw.rect(screen, dark_gray, (545, 0, 15, 600))
    pygame.draw.line(screen, yellow, (75, 0), (75, 600), 5)
    pygame.draw.line(screen, yellow, (525, 0), (525, 600), 5)
    for i in range(225, 525, 150):
        pygame.draw.line(screen, white, (i, 60), (i, 180), 10)
        pygame.draw.line(screen, white, (i, 240), (i, 360), 10)
        pygame.draw.line(screen, white, (i, 420), (i, 540), 10)     
def display_coin_corner(x, y):
    screen.blit(coin_corner, (x, y))
    screen.blit(font.render(str(score), True, white), (x + 100, y))
def display_hearts(x, y):
    for i in range(hearts):
        screen.blit(heart, (x, y))
        x += 20
def display_mycar(mycar_x, mycar_y):
    screen.blit(my_car, (mycar_x, mycar_y))
def display_oncoming(oncoming_x, oncoming_y):
    screen.blit(oncoming, (oncoming_x, oncoming_y))
def display_coin(coin_x, coin_y):
    screen.blit(coin, (coin_x, coin_y))
def oncoming_collision(mycar_x, mycar_y, oncoming_x, oncoming_y):
    if mycar_x in range(oncoming_x - 60, oncoming_x + 60) and mycar_y in range(oncoming_y - 140, oncoming_y + 140):
        return True
    return False
def coin_collision(mycar_x, mycar_y, coin_x, coin_y):
    if mycar_x in range(coin_x - 60, coin_x + 50) and mycar_y in range(coin_y - 140, coin_y + 50):
        return True
    return False
def coin_oncoming_collision(coin_x, coin_y, oncoming_x, oncoming_y):
    if coin_x in range(oncoming_x - 60, oncoming_x + 60) and coin_y in range(oncoming_y - 140, oncoming_y + 140):
        return True
    return False
def the_end(x, y):
    screen.blit(gameover, (0, 0))
    screen.blit(font.render("Your record:", True, white), (x, y))
    screen.blit(font.render(str(score), True, white), (x + 270, y))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_1:
                oncoming = pygame.image.load("./images/police.png")
            if event.key == pygame.K_2:
                oncoming = pygame.image.load("./images/taxi.png")
            if event.key == pygame.K_3:
                oncoming = pygame.image.load("./images/ambulance.png")
    
    construct_background()
    
    display_mycar(mycar_x, mycar_y)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LALT] and pressed[pygame.K_F4]:
        running = False
    if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
        mycar_x -= mycar_dx
    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
        mycar_x += mycar_dx
    
    if mycar_x < 55:
        mycar_x = 55
    if mycar_x + 60 > 545:
        mycar_x = 485

    display_oncoming(oncoming_x, oncoming_y)
    oncoming_y += oncoming_dy

    if oncoming_y > 600:
        oncoming_x = random.randint(75, 465)
        oncoming_y = -150
        oncoming_dy = random.randint(1, 5)
    
    if oncoming_collision(mycar_x, mycar_y, oncoming_x, oncoming_y):
        hearts -= 1
        pygame.mixer.Sound("./sounds/crash.wav").play()
        time.sleep(0.2)
        mycar_x = 270
        time.sleep(0.2)
        oncoming_x = random.randint(75, 465)
        oncoming_y = -150
        oncoming_dy = random.randint(1, 5)
        coin_x = random.randint(75, 475)
        coin_y = -55
        
    display_coin(coin_x, coin_y)
    coin_y += coin_dy
    
    if coin_y > 600:
        coin_x = random.randint(75, 475)
        coin_y = -55
    
    if coin_collision(mycar_x, mycar_y, coin_x, coin_y):
        score += 1
        pygame.mixer.Sound("./sounds/coin_sound.mp3").play()
        coin_x = random.randint(75, 475)
        coin_y = -55
    
    if coin_oncoming_collision(coin_x, coin_y, oncoming_x, oncoming_y):
        coin_dx = [-60, 60]
        if coin_x + 50 > 475:
            coin_x += coin_dx[0]
        elif coin_x < 75:
            coin_x += coin_dx[1]
        else:
            coin_x += coin_dx[random.randint(0, 1)]
    
    display_hearts(5, 5)
    display_coin_corner(440, 2)

    if hearts == 0:
        background_sound.stop()
        time.sleep(0.1)
        the_end(130, 350)
        time.sleep(0.1)
        pygame.mixer.Sound("./sounds/losing.wav").play()
        time.sleep(0.2)
        pygame.mixer.Sound("./sounds/gameover_sound.mp3").play()
        pygame.display.flip()
        time.sleep(5)
        running = False
     
    pygame.display.flip()
    clock.tick(60)

pygame.quit()