import pgzrun
from random import randint 

WIDTH = 500
HEIGHT = 500

def draw(): 
    r = 255 
    g = 0 
    b = randint(120,255)
    w = WIDTH 
    h = HEIGHT - 200
    for i in range(25): 
        rect = Rect((0,0),(w,h))
        rect.center = 250,250
        screen.draw.rect(rect,(r,g,b))
        w = w - 10 
        h = h + 10
        r -= 10
        g += 10


    

pgzrun.go() 