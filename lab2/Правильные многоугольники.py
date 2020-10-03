import turtle as tr
import numpy as np

tr.speed(5)

def polygons(n):
	for i in range (n):
		tr.forward(f*n)
		tr.left(360/n)
	
f=10
for j in range (3,10):
	tr.right(180 * (j - 2) / j / 2)
	polygons(j)
	tr.left(180 * (j - 2) / j / 2)
	tr.up()
	tr.backward(f)
	tr.down()
tr.exitonclick()	