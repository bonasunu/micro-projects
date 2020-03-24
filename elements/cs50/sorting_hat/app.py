from flask import Flask, render_template

app = FLask(__name__)

@app.route("/")
def index("/"):
    return render_template("index.html")