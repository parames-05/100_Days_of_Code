import turtle
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
timmy.shape("classic")
timmy.speed("fastest")
def draw_spiro(gap):
        for __ in range(int(360/gap)):
            timmy.color(Random_color())
            timmy.circle(100)
            timmy.setheading(timmy.heading() + gap)
            timmy.circle(100)
draw_spiro(5)



my_screen= Screen()
my_screen.exitonclick()
