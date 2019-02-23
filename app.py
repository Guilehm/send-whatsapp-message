import os
import urllib

from flask import Flask, redirect
from flask import render_template
from flask import request

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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
