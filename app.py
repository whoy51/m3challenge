from flask import Flask, render_template
from one import us_predict

app = Flask(__name__)


@app.route('/')
def index():
    print("Hello World!")
    print(str(us_predict))
    return render_template('index.html', data=us_predict)


if __name__ == '__main__':
    app.run()
