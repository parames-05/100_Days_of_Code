from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboardnew import Scoreboard
my_scr= Screen()
my_scr.setup(600,600)
my_scr.bgcolor("black")
my_scr.title("Jungle Bungle")
my_scr.tracer(0)
food = Food()
score = Scoreboard()

snake = Snake()

my_scr.listen()
my_scr.onkey(snake.up, "Up")
my_scr.onkey(snake.down,"Down")
my_scr.onkey(snake.left,"Left")
my_scr.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    my_scr.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() >290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    for segmet in snake.segments:
        if segmet == snake.head:
            pass
        elif snake.head.distance(segmet) < 10:
            game_is_on = False
            score.game_over()





my_scr.exitonclick()