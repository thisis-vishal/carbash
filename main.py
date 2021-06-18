import time
from turtle import Screen, Turtle, exitonclick, xcor, ycor
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
score_board=Scoreboard()
screen.listen()
screen.onkey(player.go_up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #detect collison
    for car in car_manager.all_Cars:
        if car.distance(player)<20:
            game_is_on=False
            score_board.gameover()
    
    #crossed succesfully
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score_board.inc_level()
screen.exitonclick()            