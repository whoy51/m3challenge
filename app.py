from flask import Flask, render_template
import json
import data

app = Flask(__name__)


@app.route('/')
def index():
    usjs = {'data': data.us_prediction}
    ukjs = {'data': data.uk_prediction}
    usscaled = {'data': data.us_scaled}
    ukscaled = {'data': data.uk_scaled}
    return render_template('index.html', usjs=json.dumps(usjs), ukjs=json.dumps(ukjs),
                           usscaled=json.dumps(usscaled), ukscaled=json.dumps(ukscaled),
                           us_rate=data.us_average, uk_rate=data.uk_average)


if __name__ == '__main__':
    app.run()
