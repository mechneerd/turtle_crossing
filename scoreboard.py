from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-250, 250)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f'LEVEL: {self.level}')

    def after_crossing(self):
        self.level += 1
        self.score_update()
