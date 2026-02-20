import pgzrun 
from random import randint
TITLE = "Good Shot!"
message = ""
WIDTH  = 400
HEIGHT = 400

alien = Actor('alienimage')
target = Actor('target')

def draw ():
    screen.clear()
    screen.fill(color=(255,208,160))
    alien.draw()
    screen.draw.text(message, center = (300,80), fontsize = 30 )

def place_alien():
    alien.x = randint(50,WIDTH - 50)
    alien.y = randint(50,HEIGHT - 50)
def on_mouse_down(pos):
    global message 
    if alien.collidepoint(pos):
        message = "Good Shot!"
        place_alien()
    else: 
        message = "You missed! Hah!"
    


place_alien()
pgzrun.go()