from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
ball = Ball()
score_board = ScoreBoard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

player1 = Paddle()
player2 = Paddle()

player1.r_paddle()
player2.l_paddle()

screen.listen()
screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")

screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if player1.distance(ball) < 50 and ball.xcor() > 320 or player2.distance(ball) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 400:
        score_board.l_point()
        ball.c_move()
    elif ball.xcor() < -400:
        score_board.r_point()
        ball.c_move()

    if score_board.l_score ==10 or score_board.r_score ==10:
        score_board.game_over()
        game_is_on = False





screen.exitonclick()
