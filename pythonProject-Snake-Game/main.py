import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
snake = Snake()
food = Food()
score = ScoreBoard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake mania")
screen.tracer(2)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

    if snake.snake_head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        score.update_score()
        score.inc_score()

    if snake.snake_head.xcor() >280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() >280 or snake.snake_head.ycor() < -280 :
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()


