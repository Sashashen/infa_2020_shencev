import pygame as pg
from pygame.draw import *
import numpy as np

pg.init()
m=600
n=int(m*2/3)
FPS = 30
screen = pg.display.set_mode((m, n))
pi = np.pi
def ci(colour, x, y, ra, v):
    circle(screen, colour, (int(x*m/600), int(y*n/400)), int(ra*m/600), int(v*m/600))

def re(colour, x, y, l1, d1, v2):
    rect(screen, colour, (int(x*m/600), int(y*n/400), int(l1*m/600), int(d1*n/400)), v2)

def po(colour, x1, y1, x2, y2, x3, y3, x4, y4, v3):
    polygon(screen, colour,[(int(x1*m/600), int(y1*n/400)), (int(x2*m/600), int(y2*n/400)),
                                  (int(x3*m/600), int(y3*n/400)), (int(x4*m/600), int(y4*n/400))], v3)

def el(colour, x, y, l2, d2, v4):
    ellipse(screen, colour, (int(x*m/600), int(y*n/400), int(l2*m/600), int(d2*n/400)), v4)
blue = (149, 224, 243)
black = (0, 0, 0)
blue2 = (67, 54, 229)
yellow = (243, 233, 21)
yellow2 = (255, 255, 0)
white = (255, 255, 255)
grey = (155, 166, 155)
brown = (226, 127, 7)
brown2 = (183, 86, 17)
brown3 = (225, 188, 141)
brown4 = (190, 100, 27)
red = (252, 93, 93)
blue3 = (131, 95, 204)
black2 =(61, 61, 61)
black3 = (64, 63, 62)
#фон
re(blue, 0, 0, m, 170, 0)
re(blue2, 0, 170, m, 100, 0)
re(yellow, 0, 270, m, 150, 0)

#берег
a = []
for i in range(0, m):
    a.append((i, int(260*n/400 + 10*n * np.sin(i * np.pi / 60)/400)))
a.append((m, int(290*n/400)))
a.append((0, int(290*n/400)))
polygon(screen, yellow, a, 0)

def el1(x0,y0,A,B):#куруг с обводкой
    el(white, x0, y0, A, B, 0)
    el(grey, x0, y0, A, B, 1)
#облако
def cloud(x0,y0,A,B):
    el1(x0, y0, A, B)
    el1(x0+30*A/53, y0, A, B)
    el1(x0-5*A/53, y0+25*B/60, A, B)
    el1(x0+25*A/53, y0+25*B/60, A, B)
    el1(x0+55*A/53, y0+25*B/60, A, B)
    el1(x0+60*A/53, y0, A, B)
    el1(x0+75*A/53, y0+25*B/60, A, B)
cloud(230, 10, 53, 60)
cloud(60, 95, 55, 35)
cloud(100, 30, 35, 35)

#солнышко
for i in range(19):
    f = i * np.pi / 18
    x1 = 530 + 50 * np.cos(f)
    y1 = 60 - 50 * np.sin(f)
    x2 = 530 + 50 * np.cos(np.pi * 2 / 3 + f)
    y2 = 60 - 50 * np.sin(np.pi * 2 / 3 + f)
    x3 = 530 + 50 * np.cos(np.pi * 4 / 3 + f)
    y3 = 60 - 50 * np.sin(np.pi * 4 / 3 + f)
    po(yellow2, x1, y1, x2, y2, x3, y3, x1, y1, 0)

def umbrella(x,y,r):
    re(brown, x, y, r, r*160/7, 0)
    po(red, x, y, x-r*80/7, y+r*33/7, x+r*87/7, y+r*33/7, x+r, y, 0)
    po(black2, x, y, x-r*60/7, y+r*33/7, x-r*40/7, y+r*33/7, x, y, 1)
    po(black2, x, y, x-r*40/7, y+r*33/7, x-r*20/7, y+r*33/7, x, y, 1)
    po(black2, x+r, y, x+r*27/7, y+r*33/7, x+r*47/7, y+r*33/7, x+r, y, 1)
    po(black2, x+r, y, x+r*47/7, y+r*33/7, x+r*67/7, y+r*33/7, x+r, y, 1)
    re(blue3, x, y, r, 34*r/7, 1)
    po(brown, x-r*80/7, y+r*33/7, x+r*47/7, y+r*33/7, x+r*67/7, y+r*33/7, x-r*80/7, y+r*33/7, 0)
umbrella(110, 220, 7)
umbrella(230, 260, 4)
def ship(x, y, r):
    re(brown2, x, y, r, 32*r/170, 0)
    po(brown2, x + r, y, x + r, y + 31*r/170, x + 230*r/170, y, x + r, y, 0)
    re(black, x + 65*r/170, y-94*r/170, 6*r/170,94*r/170, 0)
    po(brown3, x + 71*r/170, y-94*r/170, x + 111*r/170, y-47*r/170, x + 83*r/170, y-47*r/170, x + 71*r/170, y-94*r/170, 0)
    po(brown3, x + 71*r/170, y, x + 111*r/170, y-47*r/170, x + 83*r/170, y-47*r/170, x + 71*r/170, y, 0)
    po(black3, x + 71*r/170, y-94*r/170, x + 111*r/170, y-47*r/170, x + 83*r/170, y-47*r/170, x + 71*r/170, y-94*r/170, 1)
    po(black3, x + 72*r/170, y, x + 111*r/170, y-47*r/170, x + 83*r/170, y-47*r/170, x + 72*r/170, y, 1)
    ci(white, x + 182*r/170, y + 12*r/170, 8*r/170, 0)
    ci(black, x + 182*r/170, y + 12*r/170, 9*r/170, 1)
    cord = [0] * m
    R = r*n*32/68000
    for i in range(m):
        cord[i] = [int(x*m/600 + R * np.cos(pi + i  * pi / m)),
                   int(y*m/600 + R * np.sin(-pi - i * pi / m))]
    polygon(screen, brown2, cord)
    re(brown4, x, y, r, 32 * r / 170, 1)
ship(335, 190, 170)
ship(165, 180, 85)
pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()