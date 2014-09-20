from flask import Blueprint, render_template

hello = Blueprint('hello', __name__)


@hello.route('/')
def hello_world():
    return render_template("index.html")

