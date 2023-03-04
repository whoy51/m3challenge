from flask import Flask, render_template
from one import *
import json

app = Flask(__name__)


@app.route('/')
def index():
    print("Hello World!")
    print(str(us_predict))
    jobj = {'data': us_predict}
    print(jobj)
    return render_template('index.html', data=json.dumps([ob.__dict__ for ob in us_predict()]))


if __name__ == '__main__':
    app.run()
