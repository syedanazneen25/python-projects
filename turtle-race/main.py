from turtle import Screen
from player import Player
import time
from cars_manager import Cars
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Game")
screen.tracer(0)

player = Player()
car_manager = Cars()
score = Score()
screen.listen()
screen.onkey(player.fd_player, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.new_car()
    car_manager.move_car()
    
    # Check for collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score.game_over()
    if player.ycor() > 280:
        player.goto(0, -280)
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()
