#!/usr/bin/python3

# from flask import Flask, render_template
import data


# app = Flask(__name__)


# @app.route('/')
def index():
    print("US prediction: " + str(data.us_prediction))
    print("US Average rate of change (in 1000s): " + str(data.us_average))
    print("")
    print("UK prediction: " + str(data.uk_prediction))
    print("UK Average rate of change (in 1000s): " + str(data.uk_average))
    # return render_template('index.html', data=data.uk_prediction)



if __name__ == '__main__':
    index()
    # app.run()
