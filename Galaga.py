import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

ship = Actor('ship')
bug = Actor('bug')
bullets = []
enemies = []
score = 0 
timer = 0 
game_over = False

for i in range(8):
    for j in range(4): 
        enemies.append(Actor('bug'))
        enemies[-1].x = 100+50*i 
        enemies[-1].y = 80+50*j 

def display_score():
    screen.draw.text(str(score),(50,30), fontsize = 50)

def draw():
    global game_over
    screen.clear()
    screen.fill(color=("dark blue"))
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    display_score()
    if game_over:
        screen.draw.text("Game Over!",(600,300), color = (255,215,0), fontsize = 60)
def place_ship():
   ship.x = 600
   ship.y = 500
def update():
    global score
    global timer
    global game_over
    timer = timer + 1 
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else: 
            bullet.y = bullet.y - 10 
    for enemy in enemies:
        enemy.y = enemy.y + 2
        if enemy.y >= HEIGHT: 
            enemy.y = -100
            enemy.x = random.randint(100,WIDTH - 100)
        for bullet in bullets: 
            if enemy.colliderect(bullet):
                score = score + 100 
                enemies.remove(enemy)
                bullets.remove(bullet)
        
    if keyboard.left:
        ship.x = ship.x - 2
    if keyboard.right: 
        ship.x = ship.x + 2
    if keyboard.up:
        ship.y = ship.y - 2
    if keyboard.down:
        ship.y = ship.y + 2 
    if keyboard.space and timer > 15: 
        bullets.append(Actor('bullet'))
        bullets[-1].x = ship.x 
        bullets[-1].y = ship.y
        timer = 0 
    if len(enemies) == 0:
        game_over = True
    if game_over: 
        return


    



place_ship()
pgzrun.go()