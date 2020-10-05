import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
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

def new_ball():
    '''
    рисует новый шарик 

    '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return x,y,r

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
            x, y, r = new_ball()
            if (x1 - x)*2 +(y1 - y)*2 <= r*2:
               i += 1
               print(i)

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()