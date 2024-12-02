from urllib import request
from flask import Flask, request, render_template

app = Flask(__name__)

games = [
    {
        'name': 'Rainbow Mutatant Slimes',
        'path': '/rainbowMutantSlimes'
    }
]

@app.route("/")
def landing():
    return render_template('landing.html', games=games)

@app.route("/tos")
def tos():
    return "<p>Please don't use this to harm anyone.</p>"

@app.route('/rainbowMutantSlimes')
def slimes():
    return render_template('slimes.html')