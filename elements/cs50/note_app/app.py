from flask import Flask, render_template, request, session
from flask_session import session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False 
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.methods == "POST"
        note = request.form.get("note")
        sessionp["notes"].append(note)

    render_template(index.html, notes=session["notes"])