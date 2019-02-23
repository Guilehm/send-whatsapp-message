from flask import Flask, redirect
from flask import render_template
from flask import request
import urllib
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['texto']
        ddd = request.form['ddd']
        number = request.form['numero']
        text_encoded = urllib.parse.urlencode({"text": text})
        url = f"https://wa.me/55{ddd}{number}?{text_encoded}"
        return redirect(url)
    return render_template('index.html', name=index)
