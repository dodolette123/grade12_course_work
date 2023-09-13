import sys

import pygame as pg
clock = pg.time.Clock()
pg.init()

screen = pg.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
random = (50,40,122)

myRect = pg.Rect(0,150,50,50)

while True:
    pg.event.pump()
    screen.fill(green)
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        myRect[1] -= 1
    if keys[pg.K_DOWN]:
        myRect[1] += 1
    if keys[pg.K_LEFT]:
        myRect[0] -= 1
    if keys[pg.K_RIGHT]:
        myRect[0] += 1
    pg.draw.rect(screen,red,myRect)
    clock.tick(30)
    pg.display.flip()