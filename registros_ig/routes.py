from registros_ig import app
from flask import render_template
from registros_ig.models import *

@app.route("/")
def index():

    registros = select_all()

    return render_template("index.html", data=registros)

@app.route("/new")
def create():
    return render_template("create.html")