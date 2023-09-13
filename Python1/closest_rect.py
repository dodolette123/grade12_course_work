import sys
from math import sqrt
import pygame as pg
clock = pg.time.Clock()
pg.init()

screen = pg.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)

myRect = pg.Rect(100,160,50,50)
myRect2 = pg.Rect(400,160,50,50)

def closest_rect(rect1,rect2):
    mx ,my = pg.mouse.get_pos()
    cx,cy = rect1.center
    distance = sqrt((mx-cx)**2 + (my-cy)**2)
    cx2,cy2 = rect2.center
    distance2 = sqrt((mx-cx2)**2 + (my-cy2)**2)

    if distance > distance2:
        return rect2
    else:
        return rect1


while True:
    pg.event.pump()
    pg.draw.rect(screen,red,myRect)
    pg.draw.rect(screen,red,myRect2)

    pg.draw.rect(screen,green,closest_rect(myRect,myRect2))    
    clock.tick(30)
    pg.display.flip()
