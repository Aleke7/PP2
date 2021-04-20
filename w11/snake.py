import pygame
import random
import time
pygame.mixer.init()
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

menu1 = pygame.image.load("./images/menu1.png")
menu2 = pygame.image.load("./images/menu2.png")
menu3 = pygame.image.load("./images/menu3.png")
background = pygame.image.load("./images/background.png")
nowalls = pygame.image.load("./images/nowalls.png")
nowalls2 = pygame.image.load("./images/nowalls2.png")
gameover = pygame.image.load("./images/gameover.png")
wall = pygame.image.load("./images/wall.png")
head_u = pygame.image.load("./images/head_u.png")
head_r = pygame.image.load("./images/head_r.png")
head_d = pygame.image.load("./images/head_d.png")
head_l = pygame.image.load("./images/head_l.png")
head_u2 = pygame.image.load("./images/head_u2.png")
head_r2 = pygame.image.load("./images/head_r2.png")
head_d2 = pygame.image.load("./images/head_d2.png")
head_l2 = pygame.image.load("./images/head_l2.png")

font = pygame.font.SysFont('Arial', 35)
menu_sound = pygame.mixer.Sound("./sounds/menu_sound.mp3")
menu_sound.play(-1)

playg = False
play1 = False
play2 = False
check_play1 = False
check_play2 = False
quitg = False
menug = False
nowallsg = False
nowallsg1 = False
easy = False
easy1 = False
medium = False
medium1 = False
hard = False
hard1 = False
pos_x, pos_y = None, None
easy_walls = []
medium_walls = []
hard_walls = []

class Snake:
    def __init__(self):
        self.size = 2
        self.size2 = 2
        self.width = 20
        self.height = 20
        self.dx = 20
        self.dx2 = 20
        self.dy = 0
        self.dy2 = 0
        self.elements = [[100, 180], [0, 0]]
        self.elements2 = [[100, 720], [0, 0]]
        self.score = 0
        self.score2 = 0
        self.added = False
        self.added2 = False
    def draw_snake(self):
        if self.dx == 20:
            screen.blit(head_r, (self.elements[0][0], self.elements[0][1]))
        if self.dx == -20:
            screen.blit(head_l, (self.elements[0][0], self.elements[0][1]))
        if self.dy == 20:
            screen.blit(head_d, (self.elements[0][0], self.elements[0][1]))
        if self.dy == -20:
            screen.blit(head_u, (self.elements[0][0], self.elements[0][1]))
        for i in range(1, self.size - 1):
            pygame.draw.rect(screen, (0, 0, 255), (self.elements[i][0], self.elements[i][1], self.width, self.height))
    def draw_snake2(self):
        if self.dx2 == 20:
            screen.blit(head_r2, (self.elements2[0][0], self.elements2[0][1]))
        if self.dx2 == -20:
            screen.blit(head_l2, (self.elements2[0][0], self.elements2[0][1]))
        if self.dy2 == 20:
            screen.blit(head_d2, (self.elements2[0][0], self.elements2[0][1]))
        if self.dy2 == -20:
            screen.blit(head_u2, (self.elements2[0][0], self.elements2[0][1]))
        for i in range(1, self.size2 - 1):
                pygame.draw.rect(screen, (255, 0, 0), (self.elements2[i][0], self.elements2[i][1], self.width, self.height))
    def add_to_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.added = False
    def add_to_snake2(self):
        self.size2 += 1
        self.score2 += 1
        self.elements2.append([0, 0])
        self.added2 = False
    def move_snake(self):
        if self.added:
            self.add_to_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
    def move_snake2(self):
        if self.added2:
            self.add_to_snake2()
        for i in range(self.size2 - 1, 0, -1):
            self.elements2[i][0] = self.elements2[i - 1][0]
            self.elements2[i][1] = self.elements2[i - 1][1]
        self.elements2[0][0] += self.dx2
        self.elements2[0][1] += self.dy2

def own_round(value, base = 20):
  return base * round(value // 20)

class Food:
    def __init__(self):
        self.x = own_round(random.randint(20, 780))
        self.y = own_round(random.randint(120, 780))
        self.image = pygame.image.load("./images/food.png")
    def draw_food(self):
        screen.blit(self.image, (self.x, self.y))

def display_score(x, y, score):
    screen.blit(font.render(str(score), True, (255, 255, 255)), (x, y))

def snake_food_collision():
    if food.x == snake.elements[0][0] and food.y == snake.elements[0][1]:
        pygame.mixer.Sound("./sounds/burp.mp3").play()
        snake.added = True
        food.x = own_round(random.randint(20, 780))
        food.y = own_round(random.randint(120, 780))
def snake_food_collision2():
    if food.x == snake2.elements2[0][0] and food.y == snake2.elements2[0][1]:
        pygame.mixer.Sound("./sounds/burp.mp3").play()
        snake2.added2 = True
        food.x = own_round(random.randint(20, 780))
        food.y = own_round(random.randint(120, 780))


def snake_collison():
    for i in snake.elements[1:-1]:
        if snake.elements[0] == i:
            return True
    return False
def snake_collison2():
    for i in snake2.elements2[1:-1]:
        if snake2.elements2[0] == i:
            return True
    return False

def game_over():
    menu_sound.stop()
    with open("./records/records.txt", 'a') as f:
        f.write(str(snake.score) + " " + str(snake2.score2) + " ")
    pygame.mixer.Sound("./sounds/losing.wav").play()
    time.sleep(0.2)
    pygame.mixer.Sound("./sounds/gameover_sound.mp3").play()
    time.sleep(0.2)
    screen.blit(gameover, (0, 0))
    if play1 and not check_play1:
        screen.blit(font.render("Your record:  " + str(snake.score), True, (0, 0, 0) ), (300, 550))
        with open("./records/records.txt", 'r') as ff:
            txt = ff.read().split()
    if play2 and not check_play2:
        screen.blit(font.render("Player 1:  " + str(snake.score), True, (0, 0, 0) ), (310, 550))
        screen.blit(font.render("Player 2:  " + str(snake2.score2), True, (0, 0, 0) ), (310, 590))
        with open("./records/records.txt", 'r') as ff:
            txt = [int(i) for i in ff.read().split()]
    screen.blit(font.render("The highest score:  " + str(max(txt)), True, (0, 0, 0) ), (250, 200))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()

def easy_level():
    for i in range(0, 800, 20):
        screen.blit(wall, (i, 100))
        screen.blit(wall, (i, 780))
        easy_walls.append([i, 100])
        easy_walls.append([i, 780])
    for i in range(100, 800, 20):
        screen.blit(wall, (0, i))
        screen.blit(wall, (780, i))
        easy_walls.append([0, i])
        easy_walls.append([780, i])

def medium_level():
    for i in range(140, 240, 20):
        screen.blit(wall, (i, 220))
        screen.blit(wall, (i, 660))
        screen.blit(wall, (i + 420, 220))
        screen.blit(wall, (i + 420, 660))
        medium_walls.append([i, 220])
        medium_walls.append([i, 660])
        medium_walls.append([i + 420, 220])
        medium_walls.append([i + 420, 660])
    for i in range(220, 320, 20):
        screen.blit(wall, (140, i))
        screen.blit(wall, (640, i))
        screen.blit(wall, (140, i + 340))
        screen.blit(wall, (640, i + 340))
        medium_walls.append([140, i])
        medium_walls.append([640, i])
        medium_walls.append([140, i + 340])
        medium_walls.append([640, i + 340])
def hard_level():
    for i in range(40, 800, 100):
        for j in range(140, 800, 60):
            screen.blit(wall, (i, j))
            hard_walls.append([i, j])

def wall_colision_1():
    if snake.elements[0] in easy_walls:
        pygame.mixer.Sound("./sounds/hit1.mp3").play()
        return True
    return False
def wall_colision_1_2():
    if snake2.elements2[0] in easy_walls:
        pygame.mixer.Sound("./sounds/hit1.mp3").play()
        return True
    return False

def wall_collision_2():
    if snake.elements[0] in medium_walls:
        pygame.mixer.Sound("./sounds/hit1.mp3").play()
        return True
    return False
def wall_collision_2_2():
    if snake2.elements2[0] in medium_walls:
        pygame.mixer.Sound("./sounds/hit1.mp3").play()
        return True
    return False
def wall_collision_3():
    if snake.elements[0] in hard_walls:
        pygame.mixer.Sound("./sounds/hit1.mp3").play()
        return True
    return False
def wall_collision_3_2():
    if snake2.elements2[0] in hard_walls:
        pygame.mixer.Sound("./sounds/hit1.mp3").play()
        return True
    return False
def food_snake_body_collision():
    for i in range(1, snake.size - 1):
        if food.x == i[0] and food.y == i[1]:
            return True
    return False

def food_wall_collision_2():
    for i in easy_walls:
        if food.x == i[0] and food.y == i[1]:
            return True
    for i in medium_walls:
        if food.x == i[0] and food.y == i[1]:
            return True
    return False
def food_wall_collision_3():
    for i in easy_walls:
        if food.x == i[0] and food.y == i[1]:
            return True
    for i in hard_walls:
        if food.x == i[0] and food.y == i[1]:
            return True
    return False

snake = Snake()
snake2 = Snake()
food = Food()

screen.blit(menu1, (0, 0))

FPS = 5
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and snake.dx != -20:
                snake.dx = 20
                snake.dy = 0
            if event.key == pygame.K_a and snake.dx != 20:
                snake.dx = -20
                snake.dy = 0
            if event.key == pygame.K_w and snake.dy != 20:
                snake.dx = 0
                snake.dy = -20
            if event.key == pygame.K_s and snake.dy != -20:
                snake.dx = 0
                snake.dy = 20
            if event.key == pygame.K_RIGHT and snake2.dx2 != -20:
                snake2.dx2 = 20
                snake2.dy2 = 0
            if event.key == pygame.K_LEFT and snake2.dx2 != 20:
                snake2.dx2 = -20
                snake2.dy2 = 0
            if event.key == pygame.K_UP and snake2.dy2 != 20:
                snake2.dx2 = 0
                snake2.dy2 = -20
            if event.key == pygame.K_DOWN and snake2.dy2 != -20:
                snake2.dx2 = 0
                snake2.dy2 = 20
    
    if pos_x in range(275, 527) and pos_y in range(567, 667) and quitg == False:
        pygame.mixer.Sound("./sounds/click.mp3").play()
        time.sleep(0.5)
        running = False
    if pos_x in range(275, 527) and pos_y in range(430, 530) and playg == False:
        pygame.mixer.Sound("./sounds/click.mp3").play()
        pos_x, pos_y = 0, 0
        playg = True
        quitg = True
        screen.blit(menu2, (0, 0))
        pygame.display.flip()
    if pos_x in range(275, 527) and pos_y in range(430, 530) and play1 == False:
        pygame.mixer.Sound("./sounds/click.mp3").play()
        pos_x, pos_y = 0, 0
        play1 = True
        check_play2 = True
        play2 = True
        screen.blit(menu3, (0, 0))
        pygame.display.flip()           
    if pos_x in range(275, 527) and pos_y in range(567, 667) and play2 == False:
        pygame.mixer.Sound("./sounds/click.mp3").play()
        pos_x, pos_y = 0, 0
        play1 = True
        check_play1 = True
        play2 = True
        screen.blit(menu3, (0, 0))
        pygame.display.flip()
    
    if pos_x in range(275, 527) and pos_y in range(275, 375) and nowallsg == False:
        pygame.mixer.Sound("./sounds/click.mp3").play()
        nowallsg = True
        menug = False
    if pos_x in range(275, 527) and pos_y in range(407, 507) and easy == False:
        pygame.mixer.Sound("./sounds/click.mp3").play()
        easy = True
        menug = False
    if pos_x in range(275, 527) and pos_y in range(539, 639) and medium == False:
        pygame.mixer.Sound("./sounds/click.mp3").play()
        medium = True
        menug = False
    if pos_x in range(275, 527) and pos_y in range(669, 769) and hard == False:
        pygame.mixer.Sound("./sounds/click.mp3").play()
        hard = True
        menug = False

    if play1 and not check_play1:
        if pos_x in range(667, 788) and pos_y in range(15, 80) and menug == False:
            pygame.mixer.Sound("./sounds/click.mp3").play()
            pos_x, pos_y = 0, 0
            menug = True
            screen.blit(menu1, (0, 0))
            pygame.display.flip()
            playg = False
            play1 = False
            play2 = False
            quitg = False
            menug = False
            nowallsg = False
            easy = False
            medium = False
            hard = False
            check_play1 = False
            check_play2 = False
            snake.elements = [[100, 180], [0, 0]]
            snake.size = 2
            snake.score = 0
            snake.dx = 20
            snake.dy = 0
        if nowallsg:
            FPS = 10
            screen.blit(nowalls, (0, 0))
            if snake.elements[0][0] > 800:
                snake.elements[0][0] = 0
            if snake.elements[0][0] < 0:
                snake.elements[0][0] = 800
            if snake.elements[0][1] + 20 > 800:
                snake.elements[0][1] = 120
            if snake.elements[0][1] < 110:
                snake.elements[0][1] = 800
            
            snake_collison()
            snake_food_collision()
            food.draw_food()
            snake.move_snake()
            snake.draw_snake()
            display_score(180, 3, snake.score)
            pygame.display.flip()
        if easy:
            FPS = 5
            screen.blit(nowalls, (0, 0))
            if wall_colision_1():
                game_over()
            easy_level()
            snake_collison()
            snake_food_collision()
            food.draw_food()
            snake.move_snake()
            snake.draw_snake()
            display_score(180, 3, snake.score)
            pygame.display.flip()
        if medium:
            FPS = 7
            screen.blit(nowalls, (0, 0))
            if wall_colision_1() or wall_collision_2():
                game_over()
            
            easy_level()
            medium_level()
            if food_wall_collision_2():
                food.x = own_round(random.randint(20, 780))
                food.y = own_round(random.randint(120, 780))
            snake_collison()
            snake_food_collision()
            food.draw_food()
            snake.move_snake()
            snake.draw_snake()
            display_score(180, 3, snake.score)
        if hard:
            FPS = 10
            screen.blit(nowalls, (0, 0))
            if wall_colision_1() or wall_collision_3():
                game_over()  
            easy_level()
            hard_level()
            if food_wall_collision_3():
                food.x = own_round(random.randint(20, 780))
                food.y = own_round(random.randint(120, 780))
            snake_collison()
            snake_food_collision()
            food.draw_food()
            snake.move_snake()
            snake.draw_snake()
            display_score(180, 3, snake.score)
    
    if play2 and not check_play2:
        if pos_x in range(667, 788) and pos_y in range(15, 80) and menug == False:
            pygame.mixer.Sound("./sounds/click.mp3").play()
            pos_x, pos_y = 0, 0
            menug = True
            screen.blit(menu1, (0, 0))
            pygame.display.flip()
            playg = False
            play1 = False
            play2 = False
            quitg = False
            nowallsg = False
            easy = False
            medium = False
            hard = False
            check_play1 = False
            check_play2 = False
            snake.elements = [[100, 180], [0, 0]]
            snake.size = 2
            snake.score = 0
            snake.dx = 20
            snake.dy = 0
            snake2.elements2 = [[100, 720], [0, 0]]
            snake2.size2 = 2
            snake2.score2 = 0
            snake2.dx2 = 20
            snake2.dy2 = 0
        if nowallsg:
            FPS = 10
            screen.blit(nowalls2, (0, 0))
            if snake.elements[0][0] > 800:
                snake.elements[0][0] = 0
            if snake.elements[0][0] < 0:
                snake.elements[0][0] = 800
            if snake.elements[0][1] + 20 > 800:
                snake.elements[0][1] = 120
            if snake.elements[0][1] < 110:
                snake.elements[0][1] = 800
            if snake2.elements2[0][0] > 800:
                snake2.elements2[0][0] = 0
            if snake2.elements2[0][0] < 0:
                snake2.elements2[0][0] = 800
            if snake2.elements2[0][1] + 20 > 800:
                snake2.elements2[0][1] = 120
            if snake2.elements2[0][1] < 110:
                snake2.elements2[0][1] = 800
            
            if snake_collison():
                snake.elements[0] = [0, 0]
                snake.dx = 0
                snake.dy = 0
                snake.size = 2
            if snake_collison2():
                snake2.elements2[0] = [0, 0]
                snake2.dx2 = 0
                snake2.dy2 = 0
                snake2.size2 = 2
            if snake.elements[0] == [0, 0] and snake2.elements2[0] == [0, 0]:
                game_over()
            snake_food_collision()
            snake_food_collision2()
            food.draw_food()
            snake.move_snake()
            snake.draw_snake()
            snake2.move_snake2()
            snake2.draw_snake2()
            display_score(120, -5, snake.score)
            display_score(120, 45, snake2.score2)
        if easy:
            FPS = 5
            screen.blit(nowalls2, (0, 0))
            if wall_colision_1():
                snake.elements[0] = [0, 0]
                snake.dx = 0
                snake.dy = 0
                snake.size = 2
            if wall_colision_1_2():
                snake2.elements2[0] = [0, 0]
                snake2.dx2 = 0
                snake2.dy2 = 0
                snake2.size2 = 2
            if snake.elements[0] == [0, 0] and snake2.elements2[0] == [0, 0]:
                game_over()
            easy_level()
            if snake_collison():
                snake.elements[0] = [0, 0]
                snake.dx = 0
                snake.dy = 0
                snake.size = 2
            if snake_collison2():
                snake2.elements2[0] = [0, 0]
                snake2.dx2 = 0
                snake2.dy2 = 0
                snake2.size2 = 2
            if snake.elements[0] == [0, 0] and snake2.elements2[0] == [0, 0]:
                game_over()
            snake_food_collision()
            snake_food_collision2()
            food.draw_food()
            snake.move_snake()
            snake.draw_snake()
            snake2.move_snake2()
            snake2.draw_snake2()
            display_score(120, -5, snake.score)
            display_score(120, 45, snake2.score2)
            pygame.display.flip()
        if medium:
            FPS = 7
            screen.blit(nowalls2, (0, 0))
            if wall_colision_1() or wall_collision_2():
                snake.elements[0] = [0, 0]
                snake.dx = 0
                snake.dy = 0
                snake.size = 2
            if wall_colision_1_2() or wall_collision_2_2():
                snake2.elements2[0] = [0, 0]
                snake2.dx2 = 0
                snake2.dy2 = 0
                snake2.size2 = 2
            if snake.elements[0] == [0, 0] and snake2.elements2[0] == [0, 0]:
                game_over()
            easy_level()
            medium_level()
            if food_wall_collision_2():
                food.x = own_round(random.randint(20, 780))
                food.y = own_round(random.randint(120, 780))
            if snake_collison():
                snake.elements[0] = [0, 0]
                snake.dx = 0
                snake.dy = 0
                snake.size = 2
            if snake_collison2():
                snake2.elements2[0] = [0, 0]
                snake2.dx2 = 0
                snake2.dy2 = 0
                snake2.size2 = 2
            if snake.elements[0] == [0, 0] and snake2.elements2[0] == [0, 0]:
                game_over()
            snake_food_collision()
            snake_food_collision2()
            food.draw_food()
            snake.move_snake()
            snake.draw_snake()
            snake2.move_snake2()
            snake2.draw_snake2()
            display_score(120, -5, snake.score)
            display_score(120, 45, snake2.score2)
            pygame.display.flip()
        if hard:
            FPS = 11
            screen.blit(nowalls2, (0, 0))
            if wall_colision_1() or wall_collision_3():
                snake.elements[0] = [0, 0]
                snake.dx = 0
                snake.dy = 0
                snake.size = 2
            if wall_colision_1_2() or wall_collision_3_2():
                snake2.elements2[0] = [0, 0]
                snake2.dx2 = 0
                snake2.dy2 = 0
                snake2.size2 = 2
            if snake.elements[0] == [0, 0] and snake2.elements2[0] == [0, 0]:
                game_over()
            easy_level()
            hard_level()
            if food_wall_collision_3():
                food.x = own_round(random.randint(20, 780))
                food.y = own_round(random.randint(120, 780))
            if snake_collison():
                snake.elements[0] = [0, 0]
                snake.dx = 0
                snake.dy = 0
                snake.size = 2
            if snake_collison2():
                snake2.elements2[0] = [0, 0]
                snake2.dx2 = 0
                snake2.dy2 = 0
                snake2.size2 = 2
            if snake.elements[0] == [0, 0] and snake2.elements2[0] == [0, 0]:
                game_over()
            snake_food_collision()
            snake_food_collision2()
            food.draw_food()
            snake.move_snake()
            snake.draw_snake()
            snake2.move_snake2()
            snake2.draw_snake2()
            display_score(120, -5, snake.score)
            display_score(120, 45, snake2.score2)
            pygame.display.flip()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()