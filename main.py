from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


end_of_game = False
while not end_of_game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        end_of_game = True
        scoreboard.game_over()

    # Detect Collision with own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            end_of_game = True
            scoreboard.game_over()

screen.exitonclick()
