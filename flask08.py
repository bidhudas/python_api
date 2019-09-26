#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/upload", methods = ["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    if request.method == "POST":
        fattach = request.files["file"]
        fattach.save(secure_filename(fattach.filename))
        return "File uploaded successfully!"

if __name__ == "__main__":
    app.run(port = 5006)
