#!/usr/bin/env python

from flask import Flask, request, render_template, url_for, Response, json
from yhat import Yhat
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        yh = Yhat("USERNAME", "APIKEY",
                  "http://cloud.yhathq.com/")
        pred = yh.predict("BeerRec", {"beers": request.json['beers'],
                          "n": request.json['n']})
        return Response(json.dumps(pred),
                        mimetype='application/json')
    else:
        # static files
        css_url = url_for('static', filename='css/main.css')
        jquery_url = url_for('static', filename='js/jquery-1.10.2.min.js')
        beers_url = url_for('static', filename='js/beers.js')
        highlight_url = url_for('static', filename='js/code.js')
        js_url = url_for('static', filename='js/main.js')
        return render_template('index.html', css_url=css_url,
                               jquery_url=jquery_url, beers_url=beers_url,
                               js_url=js_url, highlight_url=highlight_url)

if __name__ == '__main__':
    app.run(debug=True)
