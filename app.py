#!/usr/bin/python3


from flask import Flask, render_template
import json

import data


app = Flask(__name__)


@app.route('/')
def index():
    print("US prediction: " + str(data.us_prediction))
    print("US Average rate of change (in 1000s): " + str(data.us_average))
    print("")
    print("UK prediction: " + str(data.uk_prediction))
    print("UK Average rate of change (in 1000s): " + str(data.uk_average))

    usjs = {'data': data.us_prediction}
    ukjs = {'data': data.uk_prediction}
    return render_template('index.html', usjs=json.dumps(usjs), ukjs=json.dumps(ukjs))


if __name__ == '__main__':
    app.run()
