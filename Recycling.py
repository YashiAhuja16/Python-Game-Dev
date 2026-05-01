import pgzrun
import random
WIDTH = 800
HEIGHT = 600
center = (400,300)
background = "background_image"
final_level = 6 
start_speed = 10
ITEMS = ["battery","can","plastic_bottle","styrofoam"]
game_over = False
game_complete = False 
current_level = 1
items = []
animations = []

def draw():
    global items, current_level, game_over, game_complete
    screen.blit("background_image", (0, 0))
    if game_over:
        display_message("GAME OVER","TRY AGAIN")
    elif game_complete: 
        display_message("YOU WON", "WELL DONE")
    else: 
        for item in items: 
            item.draw()

def update(): 
    global items
    if len(items) == 0:
        items = make_items(current_level)

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option)
        new_items.append(item)
    return new_items








pgzrun.go()

