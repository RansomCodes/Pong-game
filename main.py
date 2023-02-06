from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
import time


screen=Screen()
screen.bgcolor("black") 
screen.title("pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle=Paddle(coordinates=(350,0))
l_paddle=Paddle(coordinates=(-350,0))
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkeypress(key="Up",fun=r_paddle.moveup)
screen.onkeypress(key="Down",fun=r_paddle.movedown)
screen.onkeypress(key="w",fun=l_paddle.moveup)
screen.onkeypress(key="s",fun=l_paddle.movedown)

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed) 
    screen.update()
    if ball.ycor()>275 or ball.ycor()<-275:
        ball.collision_y()
    if (ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.collision_x()
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()
    ball.move()

screen.exitonclick()