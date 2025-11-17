from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("classic")
def forwards():
    timmy.forward(15)
def backwards():
    timmy.backward(15)
def clockwise():
    head = timmy.heading() + 10
    timmy.setheading(head)
def counter():
    turn = timmy.heading() -10
    timmy.setheading(turn)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

myscreen = Screen()
myscreen.listen()
myscreen.onkey(key="w",fun=forwards)
myscreen.onkey(key="s", fun=backwards)
myscreen.onkey(key="d",fun=clockwise)
myscreen.onkey(key="a", fun=counter)
myscreen.onkey(key="c", fun=clear)
myscreen.exitonclick()
