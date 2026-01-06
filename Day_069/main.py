from flask import Flask, render_template , request
import requests
import smtplib
APP_PW = "Enter_Your_Own_App_Password"
sender = "abc@gmail.com"
receiver = "abc@gmail.com"
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/ac5c83fabc076025f405").json()

app = Flask(__name__)



@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html", h1="Contact Us")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/contact',methods=["POST"])
def get_data():
    name = request.form["name"]
    email = request.form["email"]
    msg = request.form["message"]
    ph = request.form["phone"]
    subject = "You have a new notification from your blog"
    body = f"The Person trying to contact you is {name} \n {msg} \nYou can reach them at\n Phone: {ph} \n Email: {email}"
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, APP_PW)
        server.sendmail(sender, receiver, message)
        print("✅ Email sent successfully!")
    return render_template("contact.html", h1="Message Sent Successfully")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
