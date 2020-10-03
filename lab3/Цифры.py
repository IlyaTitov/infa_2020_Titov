import turtle as tr
import numpy as np
from random import *
		
def numbers(n):
	for angle, step in n[:-1]:
		tr.right(angle)
		tr.forward(step)
	last_angle, last_step = n[-1]
	tr.penup()
	tr.right(last_angle)
	tr.forward(last_step)
	tr.pendown()


def indeks(Ind):
	for i in Ind:
		numbers(dict[i])


tr.shape('turtle')
tr.color('blue')
n = 30
m = 10

n0 = ((90,2*n), (90,n), (90,2*n), (90,n), (0,n+m)) #right,forward. Последний картеж - с отрывом пера

n1 = ((-45,-np.sqrt(2)*n), (0,np.sqrt(2)*n), (-45,-2*n), (0,2*n), (90,n+m))

n4 = ((-90,-2*n), (0,n), (-90,n), (90,n), (90,2*n+m))

n7 = ((0,-n), (0,n), (-45,-np.sqrt(2)*n), (-45,-n), (0,n), (45,np.sqrt(2)*n), (45, n+m))

dict = {0: n0, 1: n1, 4: n4, 7: n7}

indeks([1, 4, 1, 7, 0, 0])



