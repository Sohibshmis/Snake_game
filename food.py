from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.count += 1
        if self.count % 5 == 0:
            self.bonus()
        else:
            self.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.color("blue")
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

    def bonus(self):
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("red")
