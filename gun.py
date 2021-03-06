from random import randrange as rnd, choice, random
import tkinter as tk
import math
import time

#print (dir(math))
x0 = 800
y0 = 600
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
g = 0.7
b = 0.02
class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color,
                tag='ball'
        )
        self.live = 30

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
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        self.vy -= g
        self.vy -= b * self.vy
        self.vx -= b * self.vx
        if self.x >= self.r + x0 or self.x <= self.r:
            self.vx = -self.vx
        if self.y >= self.r + y0 or self.y <= self.r:
            self.vy = -self.vy
        self.set_coords()
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...

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
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
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
    def __init__(self, tag):
        self.points = 0
        self.live = 1
        self.tag = tag

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        self.vx = (random() - 0.5) * 6
        self.vy = (random() - 0.5) * 6
        color = self.color = 'red'
        self.id = canv.create_oval(0, 0, 0, 0, tag=self. tag)
        self.set_coords()
        canv.itemconfig(self.id, fill=color)

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )
    def move(self):
        self.x += self.vx
        self.y -= self.vy

        if self.x <= self.r:
            self.vx = -self.vx
        if self.x >= x0 - self.r:
            self.vx = -self.vx
        if self.y <= self.r:
            self.vy = -self.vy
        if self.y >= y0 - self.r:
            self.vy = -self.vy
        self.set_coords()


targets = [target('t1'), target('t2')]
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
h = 0
score = canv.create_text(30,30,text = h ,font = '28')
def new_game(event=''):
    global gun, t1, screen1, balls, bullet, h
    for t in targets:
        t.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    any_live = 1
    for t in targets:
        t.live = 1
    while any_live or balls:
        any_live = 0

        new_balls = []
        for b in balls:
            b.move()
            if b.vx ** 2 + b.vy ** 2 < 1:
                canv.delete(b.id)
            else:
                new_balls.append(b)
                for t in targets:
                    if b.hittest(t) and t.live:
                        t.live = 0
                        canv.delete(t.tag)
                        h = h + 1
                        canv.itemconfig(score, text=h)
        balls = new_balls
        for t in targets:
            t.move()
            any_live = any_live or t.live

        if not any_live:
            canv.itemconfig(screen1, text='Вы уничтожили все цели за ' + str(bullet) + ' выстрелов')
            canv.bind('<Button-1>', '')
            canv.bind('<ButtonRelease-1>', '')
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    time.sleep(1)
    new_game()
new_game()

