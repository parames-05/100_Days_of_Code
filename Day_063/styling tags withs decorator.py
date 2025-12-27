from flask import Flask
app = Flask(__name__)

def add_bold_css(func):
    def wrapper():
        content = func()
        return f"""
        <style>
        h1 {{
            font-weight: bold;
        }}
        </style>
        {content}
        """
    return wrapper

@app.route("/")
@add_bold_css
def hello_world():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    app.run(debug=True)

