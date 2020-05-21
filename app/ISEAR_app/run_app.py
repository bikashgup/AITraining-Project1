
from flask import Flask 
from .settings import BASE_DIR
filepath = BASE_DIR +'/static'
run_app = Flask(__name__, static_folder=filepath)

from . import routes
from . import models