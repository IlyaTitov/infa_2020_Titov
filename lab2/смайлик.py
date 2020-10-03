import turtle 
def circle(g):
	for i in range(360//g):
		turtle.left(g)
		turtle.forward(5)

turtle.shape('turtle')
turtle.color('yellow')
turtle.begin_fill()
circle(2)
turtle.end_fill()

turtle.penup()
turtle.goto(-35,150)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(35,150)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(0,150)
turtle.pendown()
turtle.color('black')
turtle.begin_fill()
turtle.left(90)
turtle.backward(50)
turtle.end_fill()


turtle.penup()
turtle.goto(-30,50)
turtle.pendown()
turtle.color('red')
turtle.left(180)
for i in range(180//10):
	turtle.left(10)
	turtle.forward(5)
turtle.end_fill()

