#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/index/")
def index():
    return "Welcome to the NOT HelloWorld APIs"

@app.route("/latin")
def savlemundi():
    return "Savle mundi"

@app.route("/chinese")
def nihao():
    return "Ni hao, shijie"

@app.route("/japanese")
def kon():
    return "Kon'nichiwa sekai"

@app.route("/swahili")
def salamu():
    return "Salamu, dunia"

if __name__ == "__main__":
    app.run(port=5006)
