import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color("goldenrod")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_random = random.randint(-250, 250)
        y_random = random.randint(-250, 250)
        self.goto(x_random, y_random)

