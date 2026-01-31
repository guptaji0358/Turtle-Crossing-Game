import turtle


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)

        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05


    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    def bounce_y(self):
        self.y_move *= -1


    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.05
