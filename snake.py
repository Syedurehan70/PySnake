from turtle import Turtle

# constants below
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        # list of three square turtles
        self.tims = []
        self.create_snake()
    # since all parts are following the head so make head attribute
        self.head = self.tims[0]

# organizing initial three turtles to make look like snake
    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

# will create all the segments from 1 to 3
    def add_segment(self, pos):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.tims.append(tim)

# this part will add a segment in a position of last turtle, by holding it's position, whenever snake hits food
    # so that it grows
    def extend(self):
        self.add_segment(self.tims[-1].pos())

# function in class which cause the list of squared turtles to move in forward direction
    def move(self):
        for i in range(len(self.tims) - 1, 0, -1):
            # we want 3rd square in place of 2nd and 2nd in place of 1st,
            # so we take coordinates of the square before the that square which we want to send that location
            x_comp = self.tims[i - 1].xcor()
            y_comp = self.tims[i - 1].ycor()
            self.tims[i].goto(x_comp, y_comp)
# so 2nd part reaches the position of first, than 3rd reaches to 2nd part's position, than head moves frwd by 20
        self.head.forward(MOVE_DISTANCE)

# direction functions, making the turtle turn in certain direction if it's not facing the opposite one which we
# we asked them to follow
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
