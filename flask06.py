#!/usr/bin/python3

from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "GET":
        return redirect(url_for("signin"))
    if request.method == "POST":
        user = request.form["username"]
        
        ## figure out the TYPE of resp (how was the object instantiated)
        ## what are other attributes of resp!?
        
        resp = make_response(render_template("readcookie.html"))
        resp.set_cookie("userID", user)
        return resp

@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    #return '<h1>Welcome ' + name + '</h1>'
    return f'<h1>Welcome {name}</h1>'

if __name__ == "__main__":
    app.run(port=5006)
