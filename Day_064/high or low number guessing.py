from flask import Flask
import random as rrr
app = Flask(__name__)

num = rrr.randint(1,8)
print(num)
@app.route('/')
def home():
    return ("<h1>Welcome to the number guessing game...</h1> "
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"
            "<p>Enter a number between 1 to 8 in the url after / to guess")
@app.route('/<int:guess>')
def crt(guess):
    if guess < num:
        return ("<h1 style = 'color:purple'>Oops You guessed it too low</h1>"
                "<img src ='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")
    elif guess == num:
        return ("<h1 style='color:green'> You guessed it right Mind reader YIPPIE-KAY-YAY!!! </h1>"
                "<img src ='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />")
    else:
        return ("<h1 style ='color:red'> Oops You guessed it too high </h1>"
                "<img src ='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />")
home()

if __name__=="__main__":
    app.run(debug=True)
