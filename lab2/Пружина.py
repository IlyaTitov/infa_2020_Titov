import turtle 

def circle(g):
	for i in range(180//g):
		turtle.left(g)
		turtle.forward(10)
		
	

turtle.shape('turtle')
turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.right(90)
for i in range (10):

	circle(10)
	circle(30)