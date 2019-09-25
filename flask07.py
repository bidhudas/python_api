#!/usr/bin/python3

from flask import Flask
from flask import session
from flask import render_template
from flask import url_for
from flask import escape
from flask import request
from flask import redirect

app = Flask(__name__)
app.secret_key = "any random string you want the longer and more random the better!!!"

@app.route("/")
def index():
    if "username" in session:
        abc = session['username']
        if "visits" in session:
            session["visits"] = session.get("visits") + 1
        else:
            session["visits"] = 1
        visits = session["visits"]

        return f"Logged in as {abc} and you have been here {visits} <br> <a href = '/logout'>Click here to logout</a>"
    else:
        return f"You are not logged in. <br> <a href = '/login'>Click here to login</a>"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("sessionlogin.html")
    if request.method == "POST":
        session["username"] = request.form.get("abc")
        return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=5006)
