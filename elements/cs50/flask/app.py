from flask import Flask

app = Flask(__name__)

@app.route("/<string:name>")
def index(name):
    return f"<h2>Heyya {name}!</h2>"