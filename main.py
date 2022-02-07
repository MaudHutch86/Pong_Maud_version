from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#
# POSITION = [(0, -270), (0, -230), (0, -190), (0, -150), (0, -110), (0, -70), (0, -30),
#             (0, 10), (0, 50), (0, 90), (0, 130), (0, 170), (0, 210), (0, 250), (0, 290)]

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.move_paddle_up(), "Up")
screen.onkey(r_paddle.move_paddle_down(), "Down")
screen.onkey(l_paddle.move_paddle_up(), "W")
screen.onkey(l_paddle.move_paddle_down(), "S")

""""create line in the middle"""
# for position in POSITION:
#     line = Turtle("square")
#     line.shapesize(1)
#     line.penup()
#     line.color("White")
#     line.goto(position)


game_on = True
while game_on:
    screen.update()
    ball.move()

    """"detect collision with wall"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    """"detect collision with paddle"""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > - 320:
        ball.bounce_x()

        """"Detect r paddle miss"""
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

        """"Detect l paddle miss"""
    if ball.xcor() > -380:
        ball.reset_position()
        scoreboard.r_point()

    screen.exitonclick()

# Todo 2.create and move the paddle
# Todo 3.create another paddle
# Todo 4.create the ball and make it move
# Todo 5.detect collision with wall and bounce
# Todo 6.detect collision with paddle
# Todo 7.detect when paddle misses
# Todo 8. keep score
