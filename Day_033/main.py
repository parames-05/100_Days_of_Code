import pandas, turtle
from turtle import Turtle, Screen
timmy = Turtle()
PATH = "blank_states_img.gif"
turtle.addshape(PATH)
turtle.shape(PATH)
my_scr = Screen()
my_scr.title("Name 'em all")
data = pandas.read_csv("50_states.csv")
state_list = data["state"].tolist()
guessed_state = []
missing_states = []
while len(guessed_state) < 50:
    ans = my_scr.textinput(f"Make your Guess...{len(guessed_state)}/50 states left", "Enter a state's name").title()

    if ans in state_list:
        x, y = data[data["state"] == ans][["x", "y"]].iloc[0]
        guessed_state.append(ans)
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(x,y)
        timmy.pendown()
        timmy.write(ans,font=("Courier",8,"bold"))
    if ans == "Exit":
        for state in state_list:
            if state not in guessed_state:
                missing_states.append(state)

        deets = pandas.DataFrame(missing_states)
        deets.to_csv("missing states.csv")

        break

my_scr.exitonclick()







my_scr.exitonclick()