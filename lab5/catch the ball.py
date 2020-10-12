import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

i = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
circle_coordinate = [0, 0, 0]
dx = 10
dy = 10

def move_circle(coordinate):
    global dx, dy
    x1, y1, r1, color = coordinate
    dx = - dx
    x1 += dx
    y1 += dy
    circle(screen, color, (x1, y1), r1)
    coordinate = x1, y1, r1, color
    return coordinate

def new_ball():
    '''
    рисует новый шарик 

    '''
    
    x, y, r = randint(100, 1100), randint(100, 900), randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return x, y, r, color

circle_coordinate = new_ball()

pygame.display.update()
clock = pygame.time.Clock()
finished = False    
print('Количество очков:')
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            x, y, r, color = circle_coordinate 

            if (x1 - x)*2 +(y1 - y)*2 <= r*2:
               circle_coordinate = new_ball()
               i += 1
               print(i)

    circle_coordinate = move_circle(circle_coordinate)
            
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()