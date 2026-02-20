from codehouse import CODEBASE
from flask import render_template,Flask,request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index1.html")

@app.route('/convert', methods=['POST','GET'])
def convert():

    if request.method=='POST':
        result_to_show = None
        word=request.form['text_input'].lower()
        conv=""
        for letter in word:
            conv += CODEBASE.get(letter, " ")
            conv += " "
        result_to_show=conv
        return render_template("pg1.html",morse_output=result_to_show)
    return render_template("pg1.html")

if __name__ == "__main__":
    app.run(debug=True)




