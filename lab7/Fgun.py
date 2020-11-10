from random import randrange as rnd, choice
import tkinter as tk
import math
import time


WIDTH = 800
HEIGHT = 600
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.g = 1
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 100 # шарик показывается пока live > 0

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна WIDTHхHEIGHT).
        """

        self.live -= 1 # жизнь шарика убывается при каждом кадре 
        self.vy -= self.g

        if self.x > WIDTH or self.x < 0 :
            self.vx = -  self.vx
            self.x += self.vx
            self.y -= self.vy
            self.set_coords()

        if self.y > HEIGHT- 70 or self.y < 20:
            self.vy = -  self.vy
            self.x += self.vx
            self.y -= self.vy
            self.set_coords()

        else:
            self.x += self.vx
            self.y -= self.vy
            self.set_coords()

    def delete(self):
        canv.delete(self.id)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        
        if ((obj.x - self.x) **2  + (obj.y - self.y)**2 <= (self.r + obj.r) ** 2):
            return True
        else:
            return False
    def hit_rectangle(self, obj):
        """  проверяет сталкивание с прямоугольником """


        if (obj.y1 + obj.y > self.y )  and  self.y  > obj.y  and  (obj.x < self.x  ) and obj.x1 + obj.x > self.x  :

            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7) 

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
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.live = 1 # цель отображается на экране пока live > 0
        self.vx = 0
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28') # показывает сколько в эту цель попали 
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(100, 700)
        y = self.y = rnd(100, 400)
        r = self.r = rnd(2, 50)
        vx = self.vx = rnd(10, 20)
        vy = self.vy = rnd(10, 20)

        
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """


        if self.x + self.r > WIDTH or self.x - self.r < 0 :
            self.vx = -  self.vx
            self.x += self.vx
            self.set_coords()

        if self.y + self.r > HEIGHT- 70 or self.y - self.r < 20:
            self.vy = -  self.vy
            self.x += self.vx
            self.y -= self.vy
            self.set_coords()
       
            
           
        else:
            self.x += self.vx
            self.y -= self.vy
            #vx = self.vx = rnd(0, 10)
            self.set_coords()
        

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                 self.y - self.r,
                self.x + self.r,
                self.y + self.r)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def delete(self):
        canv.coords(self.id, -10, -10, -10, -10)

class Bomb():
    def __init__(self):


        self.new_bomb()
    def new_bomb(self ):
        self.x = rnd(10, 500)
        self.y = rnd(10, 200)
        self.id = canv.create_rectangle(self.x, self.y, self.x+10, self.y+15, fill= 'black')

    def move(self):
        if self.y < HEIGHT :
            self.y += 2
            self.set_coords()
        else:
            self.delete()
    def set_coords(self):
        canv.coords(self.id, self.x, self.y, self.x+10, self.y+15)

    def delete(self):
        canv.coords(self.id, -10, -10, -5, -5)





class Rectangle:
    def __init__(self):

        self.live = 1
        self.new_rectangle()



    def new_rectangle(self):
        x = self.x = rnd(50, 500)
        y = self.y = rnd (10, 100)
        x1 = self.x1 = rnd(50, 70)
        y1 = self.y1 = rnd (50, 70)
        self.vx = 0
        self.id = canv.create_rectangle(x, y, x+x1, y+y1, fill = 'black')


    def move(self):
        if self.x + self.x1> WIDTH  :
            self.vx = -self.vx
            self.x += self.vx
            self.set_coords()


        if  self.x  < 10   :
            self.vx = -self.vx
            self.x += self.vx
            self.set_coords()
        else :
            self.x += self.vx
           
            self.set_coords()

    def set_coords(self):
        canv.coords(self.id, self.x, self.y, self.x+self.x1, self.y+self.y1)

    def hit(self):
        canv.coords(self.id, -10, -10, -10, -10)

    def delete(self):
        canv.coords(self.id, -10, -5, -10, -5)

    #def create_bomb(self):
        #global bombs
       # if self.x > 30 and self.x < 500:
        #    bomb = Bomb()
         #   bomb.new_bomb(self.x, self.y)

    


number_of_target = 1
number_of_rectangle = 1
number_of_bomb = 5
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()

targets = [0]*number_of_target
rectangles = [0]* number_of_rectangle


def new_game(event=''):
    global gun, life,  screen1, balls, bullet, bombs
    
    bullet = 0
    balls = []
    life = number_of_target
    bombs = []*number_of_rectangle

    for i in range(number_of_bomb):

        bomb = Bomb()
        bombs += [bomb]
      


# создаем цели
    for i in range(number_of_target):
        targets[i] = target() 
        targets[i].live = 1
    for i in range(number_of_rectangle):
        rectangles[i] = Rectangle()
        rectangles[i].live = 1 
        
    canv.itemconfig(screen1, text='')
# управление
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targeting)

    z = 0.03
    


    while life > 0 :
        life = 0
       
        for i in range(len(bombs)):

            bombs[i].move()    
        for b in balls:
            
            b.move()
            for j in range(len(rectangles)):
                for i in range(len(targets)):
                    if b.hittest(targets[i]) :
                        targets[i].live = 0
                        targets[i].hit()
                        targets[i].delete()
              
                    if b.hit_rectangle(rectangles[j]):
                        rectangles[j].live = 0
                        rectangles[j].delete()

                        
                       
                        #b.live = 0
                    
                    #if t2.live == 0 and t1.live == 0:   
                     #canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
            
            
        

        for i in range(len(balls)):
            print(balls[i].live)
            if balls[i].live <= 0:
                balls[i].delete()
                balls[i] = None

        for i in range(number_of_target):
            if targets[i].live > 0 :
                targets[i].move()
                life += targets[i].live
                
        for i in range(len(bombs)):
            bombs[i].move()



        for i in range(len(rectangles)):
            if rectangles[i].live > 0 :
                rectangles[i].move()
                life += rectangles[i].live 
                #if rectangles[i].x1 == 100 :
                    #bomb = Bomb()
                    #bombs += [bomb]
                    #print('Gh')




        #for i in range(number_of_target):
         #  life += targets[i].live
        balls = [ball for ball in balls if ball is not None]
        
        canv.update()
        time.sleep(0.03)
        g1.targeting()
        g1.power_up()

    for i in range(len(balls)):
            balls[i].delete()

    for i in range(len(rectangles)):
            rectangles[i].delete()
                
    if life ==  0:   
        canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')

    canv.delete(gun)
    root.after(750, new_game)


new_game()

root.mainloop()