#!/user/bin/python3
'''zach feeser'''
import requests

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<username>")
def un(username):
    return render_template("username.html.j2", xname=username)

@app.route("/astros")
def nasa():
    spacepeeps = requests.get("http://api.open-notify.org/astros.json")
    spacepeeps = spacepeeps.json()
    return render_template("astros.html.j2", astros=spacepeeps["people"])

if __name__ == "__main__":
    app.run(port=5006, host='0.0.0.0')
