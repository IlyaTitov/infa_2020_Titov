import pygame
from pygame.draw import *
from consts import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(WHITE)
circle (screen, (255, 255, 0), ( 200, 200), 100)
circle (screen, RED, ( 150, 170), 20) #eye
circle (screen, (255, 0, 0), ( 250, 170), 20)# eye
circle (screen, (0, 0, 0), ( 250, 170), 10)
circle (screen, (0, 0, 0), ( 150, 170), 10)
polygon(screen, (0, 0, 0), ([125,140] , [200,150 ], [200, 140], [125, 130]))#brows
polygon(screen, (0, 0, 0), ([225,140] , [300,130 ], [300, 145], [225, 155]))
polygon(screen, (0, 0, 0), ([150,250] , [250 ,250 ], [250, 270 ], [150, 270]))




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()