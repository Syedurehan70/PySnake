from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Arial", 12, "normal")


# inherited Class
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # score is also a turtle
        self.n = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        # turtle looks like statement
        self.write(f"Score: {self.n}", align=ALLIGNMENT, font=FONT)

    def game_over(self):
        # display at the end
        self.goto(0, 0)
        self.write("GAME OVER", align=ALLIGNMENT, font=FONT)

    def increase_the_score(self):
        # increases the score
        self.n += 1
        # clears screen so  that it updates again, and don't get overlap
        self.clear()
        self.update_scoreboard()
