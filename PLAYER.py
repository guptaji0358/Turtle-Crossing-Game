from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("green")
        self.shapesize(1.5, 1.5)

        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def go_up(self):
        self.forward(MOVE_DISTANCE)


    def go_to_start(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y


    # Change skin color
    def change_skin(self, color):
        self.color(color)
