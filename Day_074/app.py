from flask import Flask, render_template, request

app = Flask(__name__)

SHIFT_KEY = 7
USER_FILE = "users.txt"


def shift_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isprintable():
            result += chr((ord(char) + shift) % 256)
        else:
            result += char
    return result


def save_user(username, encrypted_password):
    with open(USER_FILE, "a") as f:
        f.write(f"{username}:{encrypted_password}\n")


def verify_user(username, encrypted_password):
    try:
        with open(USER_FILE, "r") as f:
            for line in f:
                stored_user, stored_pass = line.strip().split(":")
                if stored_user == username and stored_pass == encrypted_password:
                    return True
    except FileNotFoundError:
        pass
    return False


@app.route("/", methods=["GET", "POST"])
def signup():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        encrypted_password = shift_encrypt(password, SHIFT_KEY)
        save_user(username, encrypted_password)

        message = "Signup successful! You can now log in."

    return render_template("signup.html", message=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        encrypted_password = shift_encrypt(password, SHIFT_KEY)

        if verify_user(username, encrypted_password):
            message = "Login successful ✅"
        else:
            message = "Login failed ❌ Check credentials"

    return render_template("login.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
