import os

from flask import Flask, session, redirect, url_for, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissupposedtobesecretkey'
Bootstrap(app)

class LoginForm(FlaskForm):
    # Don't forget to implement invaliud form error meassages
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15, message=('Your username is too short.'))])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80, message=('Your password is too short.'))])
    remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
    fullname = StringField('Fullname', validators=[InputRequired(), Length(min=1, max=15)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Login Success'
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    return redirect("/")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return 'register Success'
    return render_template("register.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
    