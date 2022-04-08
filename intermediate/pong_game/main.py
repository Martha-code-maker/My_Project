from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))


screen.listen()
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect r paddle misses
    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect l paddle misses
    if ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
