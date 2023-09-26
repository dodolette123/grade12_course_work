import sys
import random
import pygame as pg
clock = pg.time.Clock()
pg.init()

screen = pg.display.set_mode((600,400))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)


class Ball():

  gravity = 1
 
  def __init__(self,x,y):
    self.hitbox = pg.Rect(x,y,50,50)
    self.speedy = 0

  def update(self):
    self.hitbox[1]+=self.speedy
    self.speedy +=Ball.gravity
  def draw(self):
    pg.draw.ellipse(screen,red,self.hitbox)

ball = Ball(400,300)
ball.speedy = -20

while True:
  pg.event.pump()
  keys = pg.key.get_pressed()

  screen.fill(white)
  ball.draw()
  ball.update()

  if keys[pg.K_SPACE]:
    ball.speedy = -20
  pg.display.flip()
 
  clock.tick(30)