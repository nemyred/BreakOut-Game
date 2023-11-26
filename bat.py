from turtle import Turtle


class Bat(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(1, 5)
        self.goto(0, -250)

    def move_left(self):
        self.setx(self.xcor() - 20)

    def move_right(self):
        self.setx(self.xcor() + 20)

    def restart(self):
        self.setposition(0, -250)
