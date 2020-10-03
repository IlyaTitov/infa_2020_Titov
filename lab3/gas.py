from random import randint
import turtle as t

number_of_turtles = 5
steps_of_time_number = 100


pool = [t.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.shape('circle')
    unit.penup()
    unit.speed(0)

x = [randint(-200, 200) for unit in pool]
y = [randint(-200, 200) for unit in pool]
vx = [randint(-20, 20) for unit in pool]
vy = [randint(-20, 20) for unit in pool]

dt = 1
for t in range (500):
	for until in pool:
		i = pool.index(until)
		if abs(x[i]) >200  :
			vx[i] = -vx[i]
			x[i] += vx[i]
			y[i] += vy[i]
		elif abs(y[i]) >200  :
			vy[i] = -vy[i]
			x[i] += vx[i]
			y[i] += vy[i]
		else:
			x[i] += vx[i]
			y[i] += vy[i]

		until.goto(x[i], y[i])
