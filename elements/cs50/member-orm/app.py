from flask import Flask, request, render_template
import os
from models import *

app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def main():
    db.Create_all()

@app.route('/index')
@app.route('/')
def index():
    members = Member('Nadia', 'Pucci')
    db.session.add(members)
    db.session.commit()
    return render_template('index.html')

if __name__='__main__':
    with app.app_contect():
        main()