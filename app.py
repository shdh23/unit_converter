from flask import Flask, render_template, request, redirect, url_for, session
import secrets

app = Flask("__name__")

# secret_key = secrets.token_hex(24)
# app.secret_key = secret_key

@app.route("/")
def index():
    return render_template("layout.html")

@app.route("/length", methods=["GET", "POST"])
def length():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_length(value, from_unit, to_unit)
    return render_template("length.html", result=result)

@app.route("/weight", methods=["GET", "POST"])
def weight():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_weight(value, from_unit, to_unit)
    return render_template("weight.html", result=result)

@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_temperature(value, from_unit, to_unit)
    return render_template("temperature.html", result=result)

def convert_length(value, from_unit, to_unit):
    conversions = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1,
        'kilometer': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'milligram': 0.001,
        'gram': 1,
        'kilogram': 1000,
        'ounce': 28.3495,
        'pound': 453.592,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15)
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32


if __name__ == "__main__":
    app.run(debug=True)
