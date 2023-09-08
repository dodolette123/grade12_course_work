import sys

import pygame as pg
clock = pg.time.Clock()
pg.init()

screen = pg.display.set_mode((300,300))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
random = (50,40,122)

myRect = pg.Rect(0,150,50,50)
speed = 5
while True:
  pg.event.pump()
  mx,my = pg.mouse.get_pos()
  L,M,R = pg.mouse.get_pressed()
  if L == True:
    screen.fill(red)
  elif R == True:
    screen.fill(blue)
  else:
    screen.fill(white)
  pg.draw.ellipse(screen,random,myRect)
  if myRect.collidepoint(mx,my) and L == True:
    pg.draw.ellipse(screen,green,myRect)

  print(L,M,R)
  #print(mx,my)
  clock.tick(30)
  pg.display.flip()