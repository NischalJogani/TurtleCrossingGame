import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE

    def gen_car(self):
        rand_chance = random.randint(1, 4)
        if rand_chance == 3:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            randy = random.randint(-250, 250)
            new_car.goto(300, randy)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_change(self):
        self.car_speed += MOVE_INCREMENT
