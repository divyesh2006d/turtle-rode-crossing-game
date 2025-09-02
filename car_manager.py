from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car = []


    def create_car(self):
        x = random.randint(1, 10)
        if x == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y = random.randint(-250, 250)
            new_car.goto(250, y)
            self.car.append(new_car)


    def run(self):
        for car in self.car:
            car.backward(MOVE_INCREMENT)