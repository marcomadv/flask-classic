from flask import Flask

app = Flask(__name__)

ORIGIN_DATA="data/movimientos.sqlite"

from registros_ig.routes import *
