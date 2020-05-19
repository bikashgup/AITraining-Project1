
from flask import Flask 

ISEAR_app = Flask(__name__)

from .api.routes import routes
from .api.models import models