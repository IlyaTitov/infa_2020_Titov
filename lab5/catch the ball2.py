import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
X = 0
Y = 1
R = 2
COLOR = 3
VX = 4
VY = 5


number = 10
balls = [0]*number

def new_ball():
    '''рисует новый шарик '''

    x = randint(100, 1100)
    y = randint(100, 900)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    ball = [0]*6
    ball[X] = x
    ball[Y] = y
    ball[VX] = vx
    ball[VY] = vy
    ball[R] = r
    ball[COLOR] = color
    return ball

def move_ball(ball):
    ball[X] += ball[VX]
    ball[Y] += ball[VY] 

for i, ball in enumerate(balls):
    balls[i] = new_ball()
                

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, ball in enumerate(balls):
                    balls[i] = new_ball()
                print('Click!')
    
    for ball in balls:
        move_ball(ball)


    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()