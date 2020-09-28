import pygame
from pygame.draw import *
from consts import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(WHITE)



# фон
polygon(screen, (0, 0, 0), ([0,150] , [400, 150 ], [400, 400], [0, 400]))
polygon(screen, (255, 255, 255), ([0,0] , [0, 150 ], [400, 150], [0, 0]))

#house
polygon(screen, (250, 0, 0), ([50,350] , [200, 350 ], [200, 100], [50, 100]))

# окна
polygon(screen, (0, 0, 0), ([75,280] , [95, 280 ], [95, 330], [75, 330]))
polygon(screen, (0, 0, 0), ([140,280] , [160, 280 ], [160, 330], [140, 330]))
polygon(screen, (0, 0, 0), ([105,280] , [125, 280 ], [125, 330], [105, 330]))


# луна
circle (screen, (255, 255, 0), ( 350, 50), 45)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()