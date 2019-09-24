#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/start")
@app.route("/")
def start():
    return render_template("postmaker.html")

@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form.get("nm")
    elif request.method == "GET":
        if request.args.get("nm"): # if user did ?nm=Zach
            user = request.args.get("nm")
        else:
            user = "default_user"
    return redirect(url_for("success", name=user))

if __name__ == "__main__":
    app.run(port=5006)
