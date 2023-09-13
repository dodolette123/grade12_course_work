import sys

import pygame as pg
clock = pg.time.Clock()
pg.init()

screen = pg.display.set_mode((600,600))
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)

myRect = pg.Rect(550,300,50,350)
myRect2 = pg.Rect(550,0,50,150)
bird = pg.Rect (150, 150, 50,50 )

speed = 5
flight = 0
score = 0
oldl = 0
while True:
  pg.event.pump()
  L,M,R = pg.mouse.get_pressed()

  screen.fill(white)

  if myRect[0] > 550:
    speed = -5
  if myRect[0] < 0:
    myRect = pg.Rect(550,300,50,350)
    pg.draw.rect(screen,green,myRect)

  if myRect2[0] > 550:
    speed = -5
  if myRect2[0] < 0:
    myRect2 = pg.Rect(550,0,50,150)
    pg.draw.rect(screen,green,myRect2)
    score += 1
    print(score)
    
        
  if L == True and oldl == 0:
    flight = -8
    oldl = 1

  flight += 1
  if flight > 10:
    flight = 10
  if bird.colliderect(myRect):
    myRect = pg.Rect(550,300,50,350)
    myRect2 = pg.Rect(550,0,50,150)
    bird = pg.Rect (150, 150, 50,50 )
    pg.draw.rect(screen,green,myRect)
    pg.draw.rect(screen,green,myRect2)
    pg.draw.ellipse(screen, red, bird)
    score = 0
  if bird.colliderect(myRect2):
    myRect = pg.Rect(550,300,50,350)
    myRect2 = pg.Rect(550,0,50,150)
    bird = pg.Rect (150, 150, 50,50 )
    pg.draw.rect(screen,green,myRect)
    pg.draw.rect(screen,green,myRect2)
    pg.draw.ellipse(screen, red, bird)
    score = 0

  myRect[0] += speed
  myRect2[0] += speed
  bird[1]+= flight
  
  pg.draw.rect(screen,green,myRect)
  pg.draw.rect(screen,green,myRect2)
  pg.draw.ellipse(screen, red, bird)
  oldl = L
  clock.tick(30)
  pg.display.flip()