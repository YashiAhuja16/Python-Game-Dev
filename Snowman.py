import pgzrun 
from random import randint

HEIGHT = 600
WIDTH = 1000

snowman = Actor('snowman')
gift = Actor('gift')

score = 0

def draw():
    screen.blit("winterbackground", (0,0))
    snowman.draw()
    gift.draw() 
    screen.draw.text("Score: " + str(score), center=(60,30), fontsize=30)

def place_snowman():
    snowman.x = randint(50, WIDTH - 50)
    snowman.y = randint(50, HEIGHT - 50)

def place_gift():
    gift.x = randint(50, WIDTH - 50)
    gift.y = randint(50, HEIGHT - 50)

def update():
    global score
    
    if keyboard.left:
        snowman.x -= 2 
    if keyboard.right:
        snowman.x += 2
    if keyboard.down:
        snowman.y += 2
    if keyboard.up:
        snowman.y -= 2
    if snowman.colliderect(gift):
        score += 1
        place_gift()

place_snowman()
place_gift()

pgzrun.go()