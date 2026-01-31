from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.text_color = "gold"   # Always visible
        self.color(self.text_color)
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.update()

    def update(self):
        self.clear()
        self.color(self.text_color)
        # Always stay top-left
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.clear()
        self.color(self.text_color)
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align="center",
            font=("Arial Black", 28, "normal")
        )

