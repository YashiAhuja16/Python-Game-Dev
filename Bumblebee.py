import pgzrun
from random import randint
TITLE = "Bumblebee Game!"
WIDTH = 400
HEIGHT = 400
score = 0

bumblebee = Actor('bumblebee')
flower = Actor('flower')


def draw():
    screen.blit("background", (0,0))
    bumblebee.draw()
    flower.draw()
    screen.draw.text("Score: "+ str(score), center = (50,30), fontsize = 30)
def place_bumblebee():
    bumblebee.x = randint(50, WIDTH - 50)
    bumblebee.y = randint(50, HEIGHT - 50)
def place_flower():
    flower.x = randint(50, WIDTH - 50 )
    flower.y = randint (50, HEIGHT - 50)
def update():
    global score
    if keyboard.left:
        bumblebee.x = bumblebee.x - 2 
    if keyboard.right: 
        bumblebee.x = bumblebee.x + 2 
    if keyboard.up:
        bumblebee.y = bumblebee.y - 2
    if keyboard.down: 
        bumblebee.y = bumblebee.y + 2 
    flower_collected = bumblebee.colliderect(flower)
    if flower_collected:
        score += 1 
        place_flower()

    


place_bumblebee()
place_flower() 

pgzrun.go()