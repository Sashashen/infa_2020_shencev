import pygame
from pygame.draw import *
import numpy as np
pygame.init()
FPS = 30
m=600
n=400
screen = pygame.display.set_mode((2 * m, 2 * m))
pi=np.pi
rect(screen, (255, 200, 150), (0, 0, m *2, n * 2))
def Palma(x, y, r):
    rect(screen, (0, 128, 0), (x, y, r, r * 3))
    rect(screen, (0, 128, 0), (x, y-r *3 - int(r * 1.1), r, int(r * 3.7)))
    z = r * 3 + int(r * 1.1)
    polygon(screen, (0, 128, 0), [(int(x + r / 2), int(y - z - r / 10-r / 6)), (int(x - r / 8), int(y - z -r / 5- r / 6)),
                                  (int(x + r / 2), int(y - 1.7 * z - r / 5)), (int(x + r / 8 + r), int(y - 1.7 * z))])
    arc(screen, (0, 128, 0), (int(x - r * 5.3), int(y - z * 0.8), int(r * 5), int(r * 4)), np.pi * 0.1, np.pi * 0.7, 3)
    arc(screen, (0, 128, 0), (int(x + 1.3 * r), int(y - z * 1.2), int(r * 5), int(r * 4)), + np.pi * 0.2, np.pi * 1, 3)
    ellipse(screen, (0, 128, 0),(int(x - 4 * r),int(y - z * 0.7),int(r / 2),int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x - 3.2 * r), int(y - z * 0.75), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x - 2.4 * r), int(y - z * 0.75), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x + 5 * r), int(y - z * 1.05), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x + 4.2 * r), int(y - z * 1.15), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x + 3.4 * r), int(y - z * 1.2), int(r / 2), int(r * 2)))
    y=y - 1.7 * z - int(r / 5)
    polygon(screen, (0, 128, 0), [(int(x + r / 2), int(y - r / 10)), (int(x + r / 2-np.cos(np.pi / 7) * r / 3), int(y - r / 10 - np.sin(np.pi / 7)*r / 3)),
             (int(x + r / 2-np.cos(np.pi / 7) * r / 3 + np.cos(5 * np.pi / 14) * z / 1.2),
              int(y - r / 10 - np.sin(np.pi / 7) * r / 3-np.sin(5 * np.pi / 14) * z / 1.2)),
                                  (int(x + r/2+np.cos(5*np.pi/14)*z/1.2), int(y - r / 10-np.sin(5*np.pi/14)*z/1.2))])
    arc(screen, (0, 128, 0), (int(x - r * 7.3), int(y), int(r * 7), int(r * 4)), np.pi * 0, np.pi * 0.7, 3)
    arc(screen, (0, 128, 0), (int(x + 1.3 * r), int(y - z * 0.3), int(r * 8), int(r * 4)), +np.pi * 0.2, np.pi * 1, 3)
    ellipse(screen, (0, 128, 0), (int(x - 5.5 * r), int(y+z*0.1), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x - 4.7 * r), int(y + z * 0.02), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x - 3.9 * r), int(y + z * 0.04), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x - 3 * r), int(y + z * 0.05), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x - 2 * r), int(y + z * 0.1), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x + 5.1 * r), int(y - z * 0.28), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x + 4.2 * r), int(y - z * 0.29), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x + 3 * r), int(y - z * 0.2), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x + 6.6 * r), int(y - z * 0.23), int(r / 2), int(r * 2)))
    ellipse(screen, (0, 128, 0), (int(x + 8 * r), int(y - z * 0.12), int(r / 2), int(r * 2)))
def Panda(x,y,r):
    ellipse(screen, (255, 255, 255), (int(x), int(y), int(r * 4), int(r * 2)))
    cord=[0]*m
    R=r*1.5
    for i in range(m):
        cord[i]=[int(R * np.cos(pi * 3 / 4-i * 1.5 * pi / m)),int(R * np.sin(pi * 3 / 4-i * 1.5 * pi / m) * 2 / 5.8)]
        cord[i][0],cord[i][1] = int(- cord[i][0] * np.cos( - pi * 2 / 3) + cord[i][1] * np.sin(- pi * 2 / 3) + x + r * 3.1),\
                                int(cord[i][1] * np.cos(- pi * 2 / 3) + cord[i][0] * np.sin(- pi * 2 / 3) + y + r * 2.1)
    polygon(screen, (0, 0, 0), cord)
    polygon(screen, (0, 0, 0), [cord[0],[int((3 * cord[0][0] + cord[m-1][0]) / 4-0.4 * r * np.sin(pi / 6)),
                                         int((3 * cord[0][1] + cord[m-1][1]) / 4 + 0.4 * r * np.cos(pi / 6))],
                                [int((cord[0][0] + cord[m-1][0]) / 2 - 0.2 * r * np.sin(pi / 6)),
                                 int((cord[0][1] + cord[m-1][1]) / 2 + 0.2 * r * np.cos(pi / 6))],
                                [int((cord[0][0] + 3 * cord[m-1][0]) / 4 - 0.4 * r * np.sin(pi / 6)),
                                 int((cord[0][1] + 3 * cord[m-1][1]) / 4 + 0.4 * r * np.cos(pi / 6))],cord[m-1]])
    polygon(screen, (0, 0, 0), [[int(x + r * 1.3), int(y + r * 2.8)], [int(x + r * 2), int(y)], [int(x + r * 2.3), int(y - r * 0.1)],
                                [int(x + r * 2.3), int(y + r * 2)],[int(x + r * 2.1), int(y + r * 3.4)],
                                [int(x + r * 1.3), int(y + r * 3.8)]])
    R=r*0.5
    for i in range(m):
        cord[i]=[int(R * np.cos(pi / 2 + i * pi / m) * 1.3 + x + r * 1.3),int(R * np.sin(pi / 2 + i * pi / m) + y + r * 3.3)]
    polygon(screen, (0, 0, 0), cord)
    polygon(screen, (0, 0, 0), [[int(x), int(y + r * 0.4)], [int(x + r), int(y + r * 0.2)], [int(x + r * 1.0), int(y + r * 2.5)],
                                [int(x + r * 0.3), int(y + r * 3.4)], [int(x - r * 0.2), int(y + r * 2.8)]])
    circle(screen, (0, 0, 0), (int(x + r * 0.85), int(y + r * 2.45)), int(r * 0.2))
    circle(screen, (0, 0, 0), (int(x + r * 0.3), int(y + r * 3.39)), int(r * 0.05))
    polygon(screen, (255, 255, 255),
            [[int(x), int(y)], [int(x + r), int(y - r * 0.65)], [int(x + r * 2.2), int(y)],
             [int(x + r * 2.0), int(y + 1.5 * r)], [int(x + r * 0.2), int(y + 1.85 * r)]])
    circle(screen, (255, 255, 255), (int(x + r * 1.05), int(y + r * 0.35)), int(r / 1))
    circle(screen, (255, 255, 255), (int(x + r * 1.5), int(y + r * 0.8)), int(r / 1.15))
    circle(screen, (0, 0, 0), (int(x + r * 1.3), int(y + r * 0.8)), int(r / 3.2))
    ellipse(screen, (0, 0, 0), (int(x+r*0.1), int(y + r * 0.6), int(r / 2.1), int(r / 1.7)))
    cord1 = [0] * m
    cord2 = [0] * m
    for i in range(m):
        cord1[i]=[int(R * np.cos(i * 2 * pi / m)), int(R * np.sin(i * 2 * pi / m) * 2 / 4.2)]
        cord2[i] = [int(R * np.cos(i * 2 * pi / m)), int(R * np.sin(i * 2 * pi / m) * 2 / 4.2)]
        cord1[i][0], cord1[i][1] = int(-cord1[i][0] * np.cos(-pi * 2 / 3) + cord1[i][1] * np.sin(-pi * 2 / 3) + x + r * 0),\
                                int(cord1[i][1] * np.cos(-pi * 2 / 3) + cord1[i][0] * np.sin(-pi * 2 / 3) + y + r * 0)
        cord2[i][0], cord2[i][1] = int(-cord2[i][0] * np.cos(pi * 2 / 3) + cord2[i][1] * np.sin(pi * 2 / 3) + x + r * 2.1), \
                                   int(cord2[i][1] * np.cos(pi * 2 / 3) + cord2[i][0] * np.sin(pi * 2 / 3) + y + r * 0)
    polygon(screen, (0, 0, 0), cord1)
    polygon(screen, (0, 0, 0), cord2)
    ellipse(screen, (0, 0, 0), (int(x + r * 0), int(y + r * 1.35), int(r / 1.3), int(r / 1.7)))
def pandaren(x,y,r):
    ellipse(screen, (255, 255, 255), (int(x), int(y), int(r * 4), int(r * 2)))
    polygon(screen, (0, 0, 0), [[int(x + 2.8 * r), int(y + 1.7 * r)], [int(x + 4 * r), int(y + r)],
                                [int(x + 4.15 * r), int(y + 2 * r)], [int(x + 3 * r), int(y + 2.6 * r)]])
    circle(screen, (0, 0, 0), (int(x + 3.7 * r), int(y + 1.8 * r)), int(r / 2.14) )
    circle(screen, (0, 0, 0), (int(x + 3.1 * r), int(y + 2.1 * r)), int(r / 1.9))
    polygon(screen, (255, 255, 255),
            [[int(x), int(y)], [int(x + r), int(y - r * 0.65)], [int(x + r * 2.2), int(y)],
             [int(x + r * 2.0), int(y + 1.5 * r)], [int(x + r * 0.2), int(y + 1.85 * r)]])
    circle(screen, (255, 255, 255), (int(x + r * 1.05), int(y + r * 0.35)), int(r / 1))
    circle(screen, (255, 255, 255), (int(x + r * 1.5), int(y + r * 0.8)), int(r / 1.15))
    circle(screen, (0, 0, 0), (int(x + r * 1.3), int(y + r * 0.8)), int(r / 3.2))
    ellipse(screen, (0, 0, 0), (int(x + r * 0.1), int(y + r * 0.6), int(r / 2.1), int(r / 1.7)))
    cord1 = [0] * m
    cord2 = [0] * m
    R = r * 0.5
    for i in range(m):
        cord1[i] = [int(R * np.cos(i * 2 * pi / m)), int(R * np.sin(i * 2 * pi / m) * 2 / 4.2)]
        cord2[i] = [int(R * np.cos(i * 2 * pi / m)), int(R * np.sin(i * 2 * pi / m) * 2 / 4.2)]
        cord1[i][0], cord1[i][1] = int(-cord1[i][0] * np.cos(-pi * 2 / 3) + cord1[i][1] * np.sin(-pi * 2 / 3) + x + r * 0), \
                                   int(cord1[i][1] * np.cos(-pi * 2 / 3) + cord1[i][0] * np.sin(
                                       -pi * 2 / 3) + y + r * 0)
        cord2[i][0], cord2[i][1] = int(-cord2[i][0] * np.cos(pi * 2 / 3) + cord2[i][1] * np.sin(pi * 2 / 3) + x + r * 2.1), \
                                   int(cord2[i][1] * np.cos(pi * 2 / 3) + cord2[i][0] * np.sin(pi * 2 / 3) + y + r * 0)
    polygon(screen, (0, 0, 0), cord1)
    polygon(screen, (0, 0, 0), cord2)
    ellipse(screen, (0, 0, 0), (int(x + r * 0), int(y + r * 1.35), int(r / 1.3), int(r / 1.7)))
    polygon(screen, (0, 0, 0),
            [[int(x + 1.9 * r), int(y + 0.7 * r)], [int(x + 2.4 * r), int(y + 1.2*r)], [int(x + 2.4 * r), int(y + 2.0 * r)],
             [int(x + 1.3 * r), int(y + 2.8 * r)], [int(x + 0.8 * r), int(y + 3.0 * r)], [int(x + 0.8 * r), int(y + 2.3 * r)],
             [int(x + 1.1 * r), int(y + 2.2 * r)], [int(x + 1.85 * r), int(y + 1.65 * r)]])
    circle(screen, (0, 0, 0), (int(x + r * 0.8), int(y + r * 2.65)), int(r * 0.35))
    cord = [0] * m
    for i in range(m):
        cord[i]=[int(r * 0.5 * np.cos(pi / 2 - i * pi / m) + x + r * 1.9),int(r * 0.5 * np.sin(pi / 2-i * pi / m) + y + r * 1.2)]
    polygon(screen, (0, 0, 0), cord)
    polygon(screen, (0, 0, 0), [[int(x), int(y + r * 0.3)], [int(x), int(y + r * 1.1)], [int(x - r * 0.4), int(y + r * 1.8)],
                                [int(x + r * 0.4),int(y + r * 2.4)], [int(x + r * 0.3),int(y + r * 2.9)], [int(x - r * 0.3),int(y + r * 2.6)],
                                [int(x - r * 0.9),int(y + r * 2.1)],[int(x - r * 0.85),int(y + r * 1.5)]])
Palma(int(m / 4), int(n * 0.8), int(m / 38))
Palma(int(m / 2), n, int(m / 34))
Palma(int(m), int(n), int(m / 19))
Palma(int(m * 1.7), int(n * 0.9), int(m / 28))
Panda(int(m*1.1), int(n*1.1), int(m / 8))
pandaren(int(m / 1.2),int(n * 1.3), int(m / 20))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()