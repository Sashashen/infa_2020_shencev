import pygame
import numpy as np
from pygame.draw import *
from random import randint
import random as rn
pygame.init()
pi = np.pi

FPS = 30
m = 1200
n = 800
screen = pygame.display.set_mode((1200, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
def P(A, B, C, cord1, R, cord2):
    l1 = (A*cord1[0] + B*cord1[1] + C)/(A**2+B**2)**0.5
    l2 = (A*cord2[0] + B*cord2[1] + C)/(A**2+B**2)**0.5
    if abs(l1) <= R and l1*l2 >= 0:
        return 1
    else:
        return 0
class Sharik:
    def  __init__(self):
        self.x = randint(100, m - 100)
        self.y = randint(100, n - 100)
        self.r = randint(30, 70)
        self.color = COLORS[randint(0, 5)]
        self.Vx = randint(-2, 2)
        self.Vy = randint(-2, 2)
    def paint_ball(self):
        '''рисует новый шарик '''
        circle(screen, self.color, (self.x, self.y), self.r)
    def move(self):
        if self.x <= 50 or self.x >= m - 50:
            self.Vx = - self.Vx
        if self.y <= 50 or self.y >= n - 50:
            self.Vy = - self.Vy
        self.x = self.x + self.Vx
        self.y = self.y + self.Vy
    def check_click(self,pos):
        if abs(self.x - pos[0]) <= self.r and abs(self.y - pos[1]) <= self.r:
            return 1
        else:
            return 0



class Kwadrat:
    def __init__(self):
        self.x1 = randint(100, m - 100)
        self.y1 = randint(100, n - 100)
        self.r1 = randint(40, 70)
        self.color1 = COLORS[randint(0, 5)]
        self.fi = rn.random() * 0.5
        self.al = rn.random() * pi
    def move(self):
        '''рисует новый квадрат '''
        self.al = self.al + self.fi
    def paint_Kwadrat(self):
        polygon(screen, self.color1, [(self.x1, self.y1), (self.x1 + int(self.r1 * np.cos(self.al)), self.y1 - int(self.r1 * np.sin(self.al))),
                               (self.x1 + int(self.r1 * np.cos(pi / 4 - self.al) * (2 ** 0.5)),
                                self.y1 + int(self.r1 * np.sin(pi / 4 - self.al) * (2 ** 0.5))),
                               (self.x1 + int(self.r1 * np.sin(self.al)), self.y1 + int(self.r1 * np.cos(self.al)))], 0)
    def check_click(self, cord):
        if P(np.tan(self.al), 1, - np.tan(self.al) * self.x1 - self.y1, cord, self.r1,
             [self.x1 + int(self.r1 * np.cos(pi / 4 - self.al) * (2 ** 0.5)),
              self.y1 + int(self.r1 * np.sin(pi / 4 - self.al) * (2 ** 0.5))]) == 1:
            if P(-np.tan(self.al) ** (-1), 1, np.tan(self.al) ** (-1) * self.x1 - self.y1, cord, self.r1,
                 [self.x1 + int(self.r1 * np.cos(pi / 4 - self.al) * (2 ** 0.5)),
                  self.y1 + int(self.r1 * np.sin(pi / 4 - self.al) * (2 ** 0.5))]) == 1:
                return 1
            else:
                return 0
        else:
            return 0


pygame.display.update()
clock = pygame.time.Clock()
finished = False

k = 0
krug = []
square = []
z = -1
z1 = -1
v = 0
table = []
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            table.append(k)
            with open("highscoretable.txt") as fail:
                nomer = 0
                for line in fail:
                    nomer = 0
                    q = 1
                    while q == 1 and nomer < len(table):
                        if int(line) <= table[nomer]:
                            nomer = nomer +1
                        else:
                            q = 0
                    table.insert(nomer, int(line))
            fail = open("highscoretable.txt", 'w')
            print('records')
            for i in range(len(table)):
                fail.write(str(table[i]) + '\n')
                print(str(table[i]))

            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cord = event.pos # x,y клика
            for i in range(len(krug)):#находит верхний соответствующий круг
                if krug[i].check_click(cord) == 1:
                    z = i
            for i in range(len(square)):#находит верхний соответствующий квадрат
                if square[i].check_click(cord) == 1:
                        z1 = i
            if z != -1:
                k = k + 1
                print(k)
                krug.pop(z)
                z = -1
            if z1 != -1:
                k = k + 4
                print(k)
                square.pop(z1)
                z1 = -1
    v = v + 1
    if v % 15 == 0: #делает круги
        a = Sharik()
        a.paint_ball()
        krug.append(a)
    for i in krug:#рисует круги
        i.paint_ball()
        i.move()
    if v % 60 == 0: #делает квадраты
        b = Kwadrat()
        b.paint_Kwadrat()
        square.append(b)
    for i in square: #рисует квадраты
        i.paint_Kwadrat()
        i.move()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()