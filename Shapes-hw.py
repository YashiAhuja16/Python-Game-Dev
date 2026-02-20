import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500

def draw():
    r = 200
    g = 100
    b = randint(120,255)
    w = WIDTH
    h = HEIGHT 
    for i in range(20):
        rect = Rect((0, 0), (w, h))
        rect.center = 250, 250
        screen.draw.rect(rect, (r, g, b))

        w = w - 15
        h = h - 15
        r = r - 5
        g = g + 5

pgzrun.go()


