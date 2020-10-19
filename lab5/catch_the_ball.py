import pygame
from pygame.draw import *
from random import randint
pygame.init()
# colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
# constant for circle
X = 0
Y = 1
R = 2
COLOR = 3
VX = 4
VY = 5
# constant for rect
X1 = 0
Y1 = 1
X2 = 2
Y2 = 3
DX = 4
DY = 5
g = 5 #vertical acceleration of the rectangle

WIDTH = 1200
HEIGHT= 500

FPS = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))


number_of_circle = 10 
balls = [0]*number_of_circle 
number_of_rectangle = 5
rects = [0] *number_of_rectangle

def new_rect():
	''' The function creat new rectangle
		X1, Y1 -coordinates of the upper corner of the rectangle
		dx, dy - change of x1, y1 
	'''

	rect = [0]*6
	rect[X1] = randint(0, WIDTH) 
	rect[Y1] = randint (0, HEIGHT)
	rect[X2] = randint(10, 50) 
	rect[Y2] =randint (10, 50)
	rect[DX] = randint (0, 20)
	rect[DY] = randint (0, 20)
	return rect

def move_rect(rect):
	x = rect[X1]
	y = rect[Y1]
	x1 = rect[X2]
	y1 = rect[Y2]
	dx = rect[DX]
	dy = rect[DY]

	if x < 0 or x  > WIDTH :
		dx = -dx
		dy = randint(-20,20) # random bounce
		x +=dx
		y +=dy 

	
	if y < 0 or y  > HEIGHT :
		dy = -dy 
		dx = randint(-20,20) # random bounce
		x +=dx
		y +=dy 
		
	dy += g	
	x +=dx
	y +=dy
	
	rect[X1] = x 
	rect[Y1] = y
	rect[X2] = x1
	rect[Y2] = y1
	rect[DX] = dx
	rect[DY] = dy


	return rect

def draw_rect(rect):

	pygame.draw.rect(screen, (255, 255, 255), (rect[X1], rect[Y1], rect[X2], rect[Y2] ))

def draw(ball):

	circle(screen,ball[COLOR],(ball[X],ball[Y]),ball[R])


def new_ball():

	'''draws new ball 
		x , y - coordinate of center of the circle
		r - radius
		vx, vy - speed 
	'''

	x = randint(10, WIDTH-50)
	y = randint(10, HEIGHT-50)
	vx = randint(-10, 10)
	vy = randint(-10, 10)
	r = randint(10, 50)
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
	r = ball[R]
	x = ball[X] 
	y = ball[Y] 
	vx = ball[VX]
	vy = ball[VY]	
	if x + r > WIDTH or x - r < 0:
		vx = -vx
		x += vx
		y += vy
	if y + r > HEIGHT or y - r < 0:
		vy = -vy
		x += vx
		y += vy
	else:
		x += vx
		y += vy

	ball[X] = x
	ball[Y] = y
	ball[VX] = vx
	ball[VY] = vy	
	return ball



print('Здравствуйте. Введите число играков')
player = int(input())
out = open('result.txt' ,'w')
name = [] # list of players' name
k = 0
for k in range (player):
	# счетчики очков
	point_circle = 0
	point_rec = 0
	time = 0
	print ('Ваше имя')
	name.append(input())


	for i, ball in enumerate(balls):
		balls[i] = new_ball()

	for i, rect in enumerate(rects):
		rects[i] = new_rect()
					

	pygame.display.update()
	clock = pygame.time.Clock()
	print('Очки: ')
	while time < 300:
		time += 1
		clock.tick(FPS)
		for event in pygame.event.get():
			
			if event.type == pygame.MOUSEBUTTONDOWN:

				for i,ball in enumerate(balls): 
					x1, y1 = event.pos
					x = ball[X]
					y = ball[Y]
					r = ball[R]
					if (x- x1)**2 + (y - y1)**2 <= r**2:
						balls[i] = new_ball()
						point_circle += 1
						print(point_circle , ' ', point_rec)

				for i, rect in enumerate(rects):
					x3, y3 = event.pos
					x1 = rect[X1]
					y1 = rect[Y1]
					x2 = rect[X2]
					y2 = rect[Y2]
					if  x3  < x2 + x1 and y3  < y2 + y1  and x3 > x1 and y3 > y1:
						rects[i] = new_rect()
						if x1 < 30 : point_rec += 20
						else: point_rec += 10
						print(point_circle , ' ', point_rec)

		
		for ball in balls:
			ball = move_ball(ball)
			draw(ball)
			
		for rect in rects	:	
			rect = move_rect(rect)
			draw_rect(rect)	

		pygame.display.update()
		screen.fill(BLACK)
	print ('Результаты', name[k],' :',point_circle, point_rec,' Сумма очков :', point_rec+point_circle, file = out)
	

out.close()
pygame.quit()