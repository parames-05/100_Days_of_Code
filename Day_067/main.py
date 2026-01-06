from flask import Flask, render_template
import datetime as dt
import random as rrr
import requests
year = dt.datetime.now().year
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Type your name like /name in the url </h1>"
@app.route('/<name>')
def guesspage(name):
    number=rrr.randint(1,100)
    parameter = {
        "name":name
    }
    response = requests.get("https://api.agify.io", params=parameter).json()
    person = response["name"]
    age = response["age"]
    return render_template("index.html",yr=year,num=number, ppl=person, geee=age)

if __name__== "__main__":
    app.run(debug=True)
