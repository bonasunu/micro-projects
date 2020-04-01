import os

from flask import Flask, session, render_template, request, flash, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine('postgresql+psycopg2://ymcpeorjeoplua:5467e60fb2f7f4e42b3539a6fbef30f5423601e629f1830ba5411d5b7099c887@ec2-54-210-128-153.compute-1.amazonaws.com:5432/dbnal6csr0bchv')
db = scoped_session(sessionmaker(bind=engine))

# Login required
def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/book")
@login_required
def book():
    return render_template("book.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("sorry.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("sorry.html")

        # Ensure password and confirmation match
        elif not request.form.get("password") == request.form.get("confirmation"):
            return render_template("sorry.html")

        
        # checkUser = db.execute("SELECT username FROM users WHERE username= :user", {"user": user})
        if request.form.get("username", "password"):
            hashPass = generate_password_hash(request.form.get("password"))
            user = request.form.get("username")
            if db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", {"username": user, "hash": hashPass}):
                db.commit()
                return render_template("success.html")
            else:
                return render_template("sorry.html")

    return render_template("register.html")