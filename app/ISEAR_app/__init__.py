
from flask import Flask 

ISEAR_app = Flask(__name__)

from .api import routes