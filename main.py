from turtle import Turtle, Screen
from crossing import Cross
import time

screen = Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)
bob = Cross()

screen.listen()
screen.onkeypress(key='w', fun=bob.mv)
bob.mv()
game_on = True

while game_on:
    screen.tracer(1)
    time.sleep(.1)
    screen.update()





































screen.exitonclick()



