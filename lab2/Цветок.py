import turtle 

def circle(i):
	for j in range(120):
		turtle.forward(5)
		turtle.left(3)

	turtle.left(i)



turtle.shape('turtle')
for i in range (45,360,45):
	circle(i)

	