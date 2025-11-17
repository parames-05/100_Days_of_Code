from turtle import Turtle, Screen
import random

myscr = Screen()
myscr.setup(width=600, height=600)
myscr.title("Turtle Race!")
user_bet = myscr.textinput("Make your bet", "Who do you think will win the race? Enter a color:")


colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]


all_turtles = []


for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-250, y=y_positions[i])
    all_turtles.append(tim)


if user_bet:
    is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            distance = random.randint(1, 10)
            turtle.forward(distance)


            if turtle.xcor() >= 250:
                winning_color = turtle.pencolor()
                is_race_on = False

                if winning_color.lower() == user_bet.lower():
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle won the race.")

myscr.exitonclick()
