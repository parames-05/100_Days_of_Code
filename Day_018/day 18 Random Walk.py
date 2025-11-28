import turtle
from random import randint, randrange
from turtle import Turtle, Screen
import random as rrr
turtle.colormode(255)
def Random_color():
    r= rrr.randint(0,255)
    g= rrr.randint(0,255)
    b= rrr.randint(0,255)
    color=(r,g,b)
    return color

timmy = Turtle()
timmy.shape("turtle")
directions = [0,90,180,270]
timmy.speed("fastest")
for __ in range(70):
    timmy.pensize(10)
    timmy.forward(40)
    timmy.setheading(rrr.choice(directions))
    timmy.color(Random_color())

my_screen= Screen()
my_screen.exitonclick()
