from turtle import Turtle


class Ball(Turtle):
    def __init__(self, number):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.setposition(0, -200)
        self.setheading(-65)
        self.set_direction(number)
        self.speed('fastest')
        self.move_speed = .05

    def restart(self, number):
        self.setposition(0, -200)
        self.set_direction(number)

    def set_direction(self, number):
        self.setheading(number)

    def speed_up(self):
        self.move_speed*=.005
