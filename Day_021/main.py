#Taking rgb values as a tuple from an image using the colorgram module :)
# import colorgram as clrg
# colors = clrg.extract('img101.jpg',10)
# clr=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     newclr=(r,g,b)
#     clr.append(newclr)
# print(clr)
# The printed value is copied and pasted as colors[]....athunaala dhan, all this program lines are commented out
import turtle
from turtle import Turtle, Screen
import random as rrr
turtle.colormode(255)
timmy = Turtle()
timmy.hideturtle()
timmy.speed("fast")
x = -250
y = -200
colors = [(232, 153, 77), (218, 231, 218), (232, 203, 99), (126, 170, 141), (138, 114, 80), (4, 4, 4), (237, 134, 154)]
for xyz in range (10):
    timmy.penup()
    timmy.goto(x,y)
    timmy.pendown()
    y+=50
    for ____ in range(10):
        timmy.dot(15,rrr.choice(colors))
        timmy.penup()
        timmy.fd(50)
        timmy.pendown()


myscreen = Screen()
myscreen.exitonclick()
