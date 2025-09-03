import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

m = CarManager()
p = Player()
score = Scoreboard()
screen.listen()

screen.onkey(fun = p.move,key = "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    m.create_car()
    m.run()

    #detect collision with car
    for car in m.car:
        if car.distance(p) < 20:
            game_is_on = False


    #detect finish line
    if p.is_finishline():
        p.start()
        m.level_up()

screen.exitonclick()