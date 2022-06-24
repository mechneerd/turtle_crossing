from turtle import Turtle


class CrossTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.color('white')
        self.penup()
        self.goto(0, -280)

    def mv(self):
        self.fd(20)

    def turtle_bact_to_bottom(self):
        self.goto(0, -280)

