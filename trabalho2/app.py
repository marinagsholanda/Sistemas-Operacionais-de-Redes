from flask import Flask, redirect, render_template, request
import math


app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/static/index.html")

@app.route("/celsius/")
def cel():
    return render_template('celsius.html', titulo='Conversor de Temperaturas')

@app.route("/celsius/data/", methods=['POST'])
def form_cel():
    if request.method == 'POST':
        celsius = float(request.form['celsius'])
        temperatura = request.form['temperatura']
        if temperatura == "fahrenheit":
            celsius_fahrenheit = float((celsius * 1.8) + 32)
            msg = "A temperatura em fahrenheit é {}".format(celsius_fahrenheit)
        elif temperatura == "kelvin":
            celsius_kelvin = float((celsius + 273))
            msg = "A temperatura em kelvin é {}".format(celsius_kelvin)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg


@app.route("/fahrenheit/")
def fahr():
    return render_template('fahrenheit.html', titulo='Conversor de Temperaturas')

@app.route("/fahrenheit/data/", methods=['POST'])
def form_fahr():
    if request.method == 'POST':
        fahrenheit = float(request.form['fahrenheit'])
        temperatura = request.form['temperatura']
        if temperatura == "celsius":
            fahrenheit_celsius = float((fahrenheit - 32) / 1.8)
            msg = "A temperatura em celsius é {}".format(fahrenheit_celsius)
        elif temperatura == "kelvin":
            fahrenheit_kelvin = float(((fahrenheit - 32) * (5/9)) + 273)
            msg = "A temperatura em kelvin é {}".format(fahrenheit_kelvin)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg


@app.route("/kelvin/")
def kel():
    return render_template('kelvin.html', titulo='Conversor de Temperaturas')

@app.route("/kelvin/data/", methods=['POST'])
def form_kel():
    if request.method == 'POST':
        kelvin = float(request.form['kelvin'])
        temperatura = request.form['temperatura']
        if temperatura == "celsius":
            kelvin_celsius = float(kelvin - 273)
            msg = "A temperatura em celsius é {}".format(kelvin_celsius)
        elif temperatura == "fahrenheit":
            kelvin_fahrenheit = float(((kelvin - 273) * 1.8) + 32)
            msg = "A temperatura em fahrenheit é {}".format(kelvin_fahrenheit)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg


@app.route("/quilometros/")
def km():
    return render_template('quilometros.html', titulo='Conversor de Comprimento')

@app.route("/quilometros/data/", methods=['POST'])
def form_km():
    if request.method == 'POST':
        quilometros = float(request.form['quilometros'])
        comp = request.form['comprimento']
        if comp == "metros":
            quilometros_metros = float(quilometros * 1000)
            msg = "O comprimento em metros é {}".format(quilometros_metros)
        elif comp == "centimetros":
            quilometros_centimetros = float(quilometros * 100000)
            msg = "O comprimento em centímetros é {}".format(quilometros_centimetros)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg


@app.route("/metros/")
def m():
    return render_template('metros.html', titulo='Conversor de Comprimento')

@app.route("/metros/data/", methods=['POST'])
def form_m():
    if request.method == 'POST':
        metros = float(request.form['metros'])
        comp = request.form['comprimento']
        if comp == "quilometros":
            metros_quilometros = float(metros / 1000)
            msg = "O comprimento em quilometros é {}".format(metros_quilometros)
        elif comp == "centimetros":
            metros_centimetros = float(metros * 100)
            msg = "O comprimento em centímetros é {}".format(metros_centimetros)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg


@app.route("/centimetros/")
def cm():
    return render_template('centimetros.html', titulo='Conversor de Comprimento')

@app.route("/centimetros/data/", methods=['POST'])
def form_cm():
    if request.method == 'POST':
        centimetros = float(request.form['centimetros'])
        comp = request.form['comprimento']
        if comp == "quilometros":
            centimetros_quilometros = float(centimetros / 100000)
            msg = "O comprimento em quilometros é {}".format(centimetros_quilometros)
        elif comp == "metros":
            centimetros_metros = float(centimetros / 100)
            msg = "O comprimento em metros é {}".format(centimetros_metros)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg


@app.route("/quilogramas/")
def kg():
    return render_template('quilogramas.html', titulo='Conversor de Massa')

@app.route("/quilogramas/data/", methods=['POST'])
def form_kg():
    if request.method == 'POST':
        quilogramas = float(request.form['quilogramas'])
        massa = request.form['massa']
        if massa == "gramas":
            quilogramas_gramas = float(quilogramas * 1000)
            msg = "A massa em gramas é {}".format(quilogramas_gramas)
        elif massa == "miligramas":
            quilogramas_miligramas = float(quilogramas * 1000000)
            msg = "A massa em miligramas é {}".format(quilogramas_miligramas)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg


@app.route("/gramas/")
def g():
    return render_template('gramas.html', titulo='Conversor de Massa')

@app.route("/gramas/data/", methods=['POST'])
def form_g():
    if request.method == 'POST':
        gramas = float(request.form['gramas'])
        massa = request.form['massa']
        if massa == "quilogramas":
            gramas_quilogramas = float(gramas / 1000)
            msg = "A massa em quilogramas é {}".format(gramas_quilogramas)
        elif massa == "miligramas":
            gramas_miligramas = float(gramas * 1000)
            msg = "A massa em miligramas é {}".format(gramas_miligramas)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg


@app.route("/miligramas/")
def mg():
    return render_template('miligramas.html', titulo='Conversor de Massa')

@app.route("/miligramas/data/", methods=['POST'])
def form_mg():
    if request.method == 'POST':
        miligramas = float(request.form['miligramas'])
        massa = request.form['massa']
        if massa == "quilogramas":
            miligramas_quilogramas = float(miligramas / 1000000)
            msg = "A massa em quilogramas é {}".format(miligramas_quilogramas)
        elif massa == "gramas":
            miligramas_gramas = float(miligramas / 1000)
            msg = "A massa em gramas é {}".format(miligramas_gramas)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg