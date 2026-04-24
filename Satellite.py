import pgzrun
from random import randint
TITLE = "Satellite Game!"

WIDTH = 700
HEIGHT = 500
satellites = []
lines = []
numberofsatellites = 8 
nextsatellite = 0

def create_satellite():
    for i in range(0,numberofsatellites):
        satellite = Actor("satellite") 
        satellite.pos = randint(40, WIDTH - 40), randint(40, HEIGHT - 40)
        satellites.append(satellite)
def draw():
    number = 1
    screen.blit("starbackground",(0,0)) 
    for satellite in satellites:
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+30))
        satellite.draw() 
        number = number + 1 
    for line in lines: 
        screen.draw.line(line[0],line[1],(255,255,255)) 
def on_mouse_down(pos):
    global nextsatellite, lines 
    if nextsatellite < numberofsatellites: 
        if satellites[nextsatellite].collidepoint(pos):
            if nextsatellite:
                lines.append((satellites[nextsatellite - 1].pos,satellites[nextsatellite].pos))
            nextsatellite = nextsatellite + 1 
        else: 
            lines = []
            nextsatellite = 0

    
create_satellite()
pgzrun.go()