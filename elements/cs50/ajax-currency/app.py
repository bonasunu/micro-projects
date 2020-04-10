import requests

from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    
    # Query for currency exchange rate
    currency = request.form.get('currency')
    res = requests.get("https://api.fixer.io/api/latest",
                     params={"base": "USD", "symbols": currency})

    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success": False})

    data = res.json()
    if currency not in data["rates"]:
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"]["currency"]})    
    
