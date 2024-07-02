from flask import Flask
from markupsafe import escape

app = Flask(__name__)  # instance of Flask class is a WSGI application

@app.route("/")  # url that triggers the function
def index():
    return "<p>index page</p>"


@app.route("/hi")
def hello():
    return "<p>Hello, World!</p>"


@app.route("/<username>")
def hello_user(username):
    return f"Hello, {escape(username)}!" 
# call escape() on user input to protect injection attacs 
# jinja do this automatically


@app.route("/hi2")
def hello2():
    return "<p>Hello, World!2</p>"
