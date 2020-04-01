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