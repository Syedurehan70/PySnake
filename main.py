# Importing all the necessary classes
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# making necessary objects and initializes them
screen = Screen()
# setting screen length and width, color, title, turning tracer off so that then part where turtles are generated
# can no be seen on screen
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Mania")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

# making turtle listen the keystrokes
screen.listen()
# binding functions and keys, functions are in snake class
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    # screen update is on, trace is on
    screen.update()
    # small delay so that we can observe the update
    time.sleep(0.1)
    # moving the snake
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:
        # food is created when food  object initialized, below func will relocate the food to random position
        food.refresh()
        # snake will grow after eating food
        snake.extend()
        # updates score as the snake touches the food
        score.increase_the_score()

    # detecting collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -295:
        game_on = False
        score.game_over()

    # detecting collision with the body
    for segments in snake.tims[1:]: # slicing through all the items of tims list after skipping first item only
        # if snake head touches any segment of snake than game over
        if snake.head.distance(segments) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
