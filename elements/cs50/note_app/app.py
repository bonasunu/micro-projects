from flask import Flask, render_template, request, session
from flask_session import session

app.config["SESSION_PERMANENT"] = False 
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

