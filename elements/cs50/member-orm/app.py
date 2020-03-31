from flask import Flask, request, render_template
import os
from models import *

app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/index')
@app.route('/')
def index():
    
