# Project - Turtl Crossing Game 
# ------------------------------

# import sys

# path = r"E:\Program Files\RobinData\PYTHON\RawData"
# sys.path.append(path)

from turtle import Screen, Turtle
from PLAYER import Player
from CAR_MANAGER import CarManager
from TURTLE_CROSIING_GAME_SCOREBOARD import Scoreboard

# ---------------- SCREEN ---------------- #

screen = Screen()
screen.title("Turtle Road Crossing Game")
screen.setup(width=900, height=700)
screen.tracer(0)

# ---------------- MENU ---------------- #

menu = Turtle()
menu.hideturtle()
menu.penup()
menu.color("lightgray")
menu.goto(-430, 260)

def draw_menu():

    menu.clear()

    menu.write(
        "H : Hide/Show Menu\n"
        "S : Skin\n"
        "B : Background\n"
        "R : Replay\n"
        "P : Pause\n"
        "Q : Quit",
        align="left",
        font=("Arial", 12, "normal")
    )

# ---------------- BG COLORS ---------------- #

bg_colors = [
    "black","white","gray","lightblue","lightgreen","pink","purple",
    "orange","yellow","cyan","brown","navy","teal","gold","violet",
    "lime","salmon","coral","khaki","plum","indigo","turquoise",
    "beige","mint","lavender","peach","maroon","olive","skyblue","tan"
]

bg_index = 0
screen.bgcolor(bg_colors[bg_index])

# ---------------- PLAYER SKINS ---------------- #

player_colors = [
    "green","blue","red","yellow","cyan",
    "orange","purple","pink","white"
]

skin_index = 0

# ---------------- OBJECTS ---------------- #

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# ---------------- GAME STATE ---------------- #

paused = False
game_over = False
menu_visible = True

# ---------------- CONTROLS ---------------- #

screen.listen()
screen.onkeypress(player.go_up, "Up")

# Pause
def toggle_pause():
    global paused
    paused = not paused

screen.onkey(toggle_pause, "p")
screen.onkey(toggle_pause, "P")

# Quit
def quit_game():
    screen.bye()

screen.onkey(quit_game, "q")
screen.onkey(quit_game, "Q")

# Toggle Menu
def toggle_menu():
    global menu_visible
    menu_visible = not menu_visible
    if menu_visible:
        draw_menu()
    else:
        menu.clear()

screen.onkey(toggle_menu, "h")
screen.onkey(toggle_menu, "H")

# Change Background
def change_bg():
    global bg_index
    bg_index = (bg_index + 1) % len(bg_colors)
    screen.bgcolor(bg_colors[bg_index])
    scoreboard.update()

screen.onkey(change_bg, "b")
screen.onkey(change_bg, "B")

# Change Skin
def change_skin():
    global skin_index
    skin_index = (skin_index + 1) % len(player_colors)
    player.change_skin(player_colors[skin_index])

screen.onkey(change_skin, "s")
screen.onkey(change_skin, "S")

# Restart
def restart_game():
    global game_over, paused, menu_visible
    game_over = False
    paused = False
    menu_visible = True

    scoreboard.clear()
    scoreboard.level = 1
    scoreboard.update()
    player.go_to_start()

    for car in cars.all_cars:
        car.hideturtle()

    cars.all_cars.clear()
    cars.car_speed = 5

    draw_menu()
    game_loop()

screen.onkey(restart_game, "r")
screen.onkey(restart_game, "R")

# ---------------- GAME LOOP ---------------- #

def game_loop():
    global paused, game_over
    screen.update()
    if game_over:
        return
    
    if paused:
        screen.ontimer(game_loop, 100)
        return
    
    # Cars
    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_over = True
            scoreboard.game_over()
            if menu_visible:
                draw_menu()
            return
        
    # Finish line
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreboard.level_up()

    screen.ontimer(game_loop, 100)

# ---------------- START ---------------- 

draw_menu()
game_loop()
screen.mainloop()
