import sys

import pygame as pg
clock = pg.time.Clock()
pg.init()

screen = pg.display.set_mode((300,300))
red = (255,0,0)
green = (0,255,0)
random = (50,40,122)

myRect = pg.Rect(0,150,50,50)
myRect2 = pg.Rect(250,150,50,50)
speed = 5
while True:
  screen.fill(red)
  if myRect[0] > 300:
    speed = -5
  if myRect[0] < 0:
    speed = 5
    
  myRect[0] += speed
  if myRect.colliderect(myRect2):
    speed = -5
  pg.draw.rect(screen,green,myRect)
  pg.draw.rect(screen,random,myRect2)

  clock.tick(30)
  pg.display.flip()