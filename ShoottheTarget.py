import pgzrun
from random import randint

TITLE = "Good Shot!"
WIDTH = 400
HEIGHT = 400
message = ""

target = Actor("target")

def draw():
    screen.clear()
    screen.fill((255, 208, 160))
    target.draw()
    screen.draw.text(message, center=(200, 30), fontsize=30)

def place_target():
    target.x = randint(50, WIDTH - 50)
    target.y = randint(50, HEIGHT - 50)

def on_mouse_down(pos):
    global message
    if target.collidepoint(pos):
        message = "Good Shot!"
        place_target()
    else:
        message = "You missed! Hah!"

place_target()
pgzrun.go()