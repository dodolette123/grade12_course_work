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
red = (255,0,0)

class Car():
    w = 75
    h = 50

    def __init__(self,x,y,color):
        self.hitbox = pg.Rect(x,y,Car.w,Car.h)
        self.speed = 0
        self.color = color
    def update(self):
        self.hitbox[0] += self.speed
    def draw(self):
        pg.draw.ellipse(screen,self.color,self.hitbox)

my_car_1 = Car(0,200,red)
my_car_2 = Car(300,100,blue)
my_car_1.speed = 5
my_car_2.speed = 10
while True:
    screen.fill(white)
    my_car_1.update()
    my_car_2.update()


    my_car_1.draw()
    my_car_2.draw()
    clock.tick(30)
    pg.display.flip()
        