import random
from turtle import Turtle


# class and inherited class is created
class Food(Turtle):
    # both initialized
    def __init__(self):
        super().__init__()
        # new turtle in shape of circle is created, for food
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)