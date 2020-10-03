import turtle 

for j in [3, 6, 9, 12, 30] :
	j=int(j)
	for i in range(360//j):
		turtle.forward(8)
		turtle.left(j)
	for i in range (360//j):
		turtle.forward(8)
		turtle.right(j)

