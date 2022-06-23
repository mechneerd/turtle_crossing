from turtle import Turtle


class Cross(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.setheading(90)
        self.penup()
        self.speed('fastest')
        self.shape('turtle')
        self.shapesize(1, 1)
        self.goto(0, -280)

    def mv(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
