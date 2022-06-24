from turtle import Turtle
from crossing import CrossTurtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class ManageCar(Turtle):

    def __init__(self):
        super().__init__()
        self.random_car = []
        self.car_speed = 10

    def build_car(self):
        car_creation_speed = random.randint(1, 6)
        if car_creation_speed == 1:
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.random_car.append(car)

    def cross_car(self):
        for i in self.random_car:
            i.backward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += 5






