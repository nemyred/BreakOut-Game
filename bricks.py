from turtle import Turtle


class Brick:
    def __init__(self):
        self.brick_list = []

    def create_brick(self, position_x, position_y, colour):
        new_brick = Turtle('square')
        new_brick.speed("fastest")
        new_brick.penup()
        new_brick.hideturtle()
        new_brick.setposition(position_x, position_y)
        new_brick.showturtle()
        new_brick.color(colour)
        new_brick.shapesize(2, 4)
        self.brick_list.append(new_brick)

    def remove_brick(self, index):
        del self.brick_list[index]
