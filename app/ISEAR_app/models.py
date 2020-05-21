from flask_cors import CORS
from flask_pymongo import PyMongo
from .run_app import run_app
from .settings import BASE_DIR
# Load Config File for DB
run_app.config.from_pyfile(BASE_DIR+'/mongo_config.cfg')
CORS(run_app)
mongo = PyMongo(run_app)

    