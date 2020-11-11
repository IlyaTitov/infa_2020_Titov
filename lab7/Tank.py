from tkinter import *
from random import randrange as rnd, choice
import math
import time
root = Tk()
c = Canvas(width=300, height=300, 
           bg='white')
c.focus_set()
c.pack()

class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        x = self.x = 10
        y = self.y = 480
        x1 = self.x1 = 30
        y1 = self.y1 = 490
        self.vx = 0
        self.id = c.create_line(x,y,x+x1,y+y1,width=7) 

    def fire2_start(self, event):
        self.f2_on = 1



    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball] # создаются список шариков 
        self.f2_on = 0
        self.f2_power = 10

    def targeting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            c.itemconfig(self.id, fill='orange')
        else:
            c.itemconfig(self.id, fill='black')
        c.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )
class Tank(gun):
	def __init__ (self):
		self.x = 20
		self.y = 135
		self.r = 5
		self.x_body = 10
		self.x1_body = 50
		self.y_body = 140
		self.y1_body = 150
		self.ball = c.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = 'black' )
		self.body = c.create_rectangle(self.x_body , self.y_body, self.x1_body, self.y1_body,fill = 'black')
	def move_right(self,event):
		c.move(self.ball,   +2, 0 )
		c.move(self.body,   +2,0 )
		c.move(self.id,   +2,0 )



	def move_left(self, event):
		c.move(self.ball,   -2, 0)
		c.move(self.body,   -2, 0)




   

g1 = gun() 
t = Tank()
c.bind('<Left>', t.move_left)
c.bind('<Motion>', g1.targeting)


c.bind('<Right>', t.move_right)
 
root.mainloop()
