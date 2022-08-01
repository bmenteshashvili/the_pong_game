from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
time_sleep=0.1
while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 :

        ball.bounce_x()
        time_sleep *= 0.09
    if ball.distance(l_paddle) < 50 and ball.xcor() < -325 :
        ball.bounce_x()
        time_sleep *= 0.09
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
        time_sleep = 0.1

    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()
        time_sleep = 0.1




















screen.exitonclick()