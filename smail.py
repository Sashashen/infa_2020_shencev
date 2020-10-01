import pygame
from pygame.draw import *
import numpy as np
pygame.init()
FPS = 30
m=200
R=130
screen = pygame.display.set_mode((2 * m, 2 * m))
color = (255, 255, 255)
rect(screen, (200, 200, 200), (0, 0, 2 * m, 2 * m))
def Circle(r, g, b, x, y, R): # круг с обводкой
    circle(screen, (0, 0, 0), (x, y), R + 2)
    circle(screen, (r, g, b), (x, y), R)
Circle(255, 255, 0, m, m, R)
Circle(255, 0, 0, m - int(R / 2), m - int(R /3), int(R / 6))
Circle(255, 0, 0, m + int(R / 2), m - int(R / 3), int(R / 7))
circle(screen, (0, 0, 0), (m - int(R / 2), m - int(R / 3)), int(R / 12))
circle(screen, (0, 0, 0), (m + int(R / 2), m - int(R / 3)), int(R / 12))
rect(screen, (0, 0, 0), (m - int(R / 2), m + int(R / 2.5), R, int(R / 5.5)))
polygon(screen, (0, 0, 0), [(m - int(R / 4), m - int(R / 2)), (m - int(R / 4) + int(np.cos(np.pi / 3) * R / 12),
                                                               m - int(R / 2) - int(np.sin(np.pi / 3) * R / 12)),
                            (m - int(R / 4) - int(np.cos(np.pi / 6) * R), m - int(R / 2) - int(np.sin(np.pi / 6) * R))])
polygon(screen, (0, 0, 0), [(m + int(R / 4), m - int(R / 2)), (m + int(R / 4) - int(np.cos(np.pi / 3) * R / 12),
                                                               m - int(R / 2) - int(np.sin(np.pi / 3) * R / 12)),
                            (m + int(R / 4) + int(np.cos(np.pi / 6) * R), m - int(R / 2) - int(np.sin(np.pi / 6) * R))])
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()