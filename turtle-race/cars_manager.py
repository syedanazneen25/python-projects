from turtle import Turtle
import random
COLORS = ["red", "blue", "yellow", "green", "black", "purple"]
MOVE_DISTANCE = 5
INCREAMENT = 10


class Cars():
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE
    def new_car(self):
        chance = random.randint(1, 6)
        if chance == 6 or chance == 5:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += INCREAMENT
