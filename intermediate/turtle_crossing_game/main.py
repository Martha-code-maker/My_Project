import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

game_player = Player()
screen.onkey(game_player.up, "w")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    if game_player.is_at_finish_line():
        game_player.set_position()
        car_manager.speed_up()

    for car in car_manager.all_cars:
        if car.distance(game_player) < 20:
            scoreboard.collision_detect()
            game_is_on = False

screen.exitonclick()
