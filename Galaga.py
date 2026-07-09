import pgzrun

WIDTH = 1200
HEIGHT = 600

ship = Actor('ship')
bullets = []
enemies = []
enemies.append(Actor('bug'))
enemies[-1].x = 10 
enemies[-1].y = -100
def draw():
    screen.clear()
    screen.fill(color=("dark blue"))
    ship.draw()
    for bullet in bullets:
        bullet.draw()
def place_ship():
   ship.x = 600
   ship.y = 500
def update():
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else: 
            bullet.y = bullet.y - 10 
    if keyboard.left:
        ship.x = ship.x - 2
    if keyboard.right: 
        ship.x = ship.x + 2
    if keyboard.up:
        ship.y = ship.y - 2
    if keyboard.down:
        ship.y = ship.y + 2 
    if keyboard.space:
        bullets.append(Actor('bullet'))
        bullets[-1].x = ship.x 
        bullets[-1].y = ship.y
    



place_ship()
pgzrun.go()