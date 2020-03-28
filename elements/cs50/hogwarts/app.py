from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    house = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
    num = random.randint(0,3)
    new_house = house[num]
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    return render_template('index.html')

if (__name__) == '__main__':
    app.run()