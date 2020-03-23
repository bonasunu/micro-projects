from flask import Flask

app = Flask(__name__)

@app.route("/<string:name>")
def index():
    return f"Heyya {name}!"