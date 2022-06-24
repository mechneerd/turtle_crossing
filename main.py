from turtle import Turtle, Screen
from crossing import CrossTurtle
from car import ManageCar
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

bob = CrossTurtle()
manage_car = ManageCar()
score = Scoreboard()

screen.listen()
screen.onkeypress(key='w', fun=bob.mv)
game_on = True


while game_on:
    time.sleep(.1)
    screen.update()


    manage_car.build_car()
    manage_car.cross_car()
    # collision with car
    for i in manage_car.random_car:
        if i.distance(bob) < 25:
            score.game_over()
            game_on = False
    #turle at other end
    if bob.ycor() > 280:
        bob.turtle_bact_to_bottom()
        manage_car.increase_car_speed()
        score.after_crossing()


screen.exitonclick()
