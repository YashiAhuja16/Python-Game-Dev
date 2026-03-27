import pgzrun 
from random import randint

HEIGHT = 350
WIDTH = 520
bee = Actor('bee')
flower = Actor('flowertiny')
score = 0

def draw():
    screen.blit("background2", (0,0))
    bee.draw()
    flower.draw() 
    screen.draw.text("Score:"+ str(score), center = (50,30), fontsize = 30)
def place_bee():
    bee.x = randint(50, WIDTH - 50)
    bee.y = randint(50, HEIGHT - 50)
def place_flower():
    flower.x = randint(50, WIDTH - 50)
    flower.y = randint(50, HEIGHT - 50)
def update():
    global score
    if keyboard.left:
        bee.x = bee.x - 2 
    if keyboard.right:
        bee.x = bee.x + 2
    if keyboard.down:
        bee.y = bee.y + 2
    if keyboard.up:
        bee.y = bee.y - 2 


place_bee()
place_flower()
pgzrun.go()
