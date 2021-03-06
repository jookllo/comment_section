
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is somebullshit my boy!'

@app.route('/webo')
def webo():
    return 'Hope this works in my mind'