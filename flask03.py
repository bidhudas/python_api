#!/usr/bin/python3
from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello administrator"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return f"Hello guest-user, {guest}"

# This is the STARTING point for a user
@app.route("/signin/<name>")
def signin(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest=name))


if __name__ == "__main__":
    app.run(port=5006)
