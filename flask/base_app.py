#base web application in flask for python

from flask import Flask

#name holds the name of the current Python module
app = Flask(__name__)

#handling HTTP requests, the decorator turns regular python into a flask view function, converting the function return value HTTP
@app.route('/')
def hello():
    return 'Hello, World!'