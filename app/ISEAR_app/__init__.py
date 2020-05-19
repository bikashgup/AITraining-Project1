
from flask import Flask 
from ...settings import BASE_DIR
filepath = BASE_DIR +'/static'
ISEAR_app = Flask(__name__, static_folder=filepath)

from .api.routes import routes
from .api.models import models