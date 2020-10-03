import turtle as tr
tr.shape('turtle')
for i in range(5):
	tr.forward(100)
	tr.left(144)
tr.speed(0)#- max
tr.penup()
tr.goto(100,100)
tr.pendown()

for i in range(11):
	tr.forward(100)
	tr.left(180 - (360//22))