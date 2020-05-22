from flask_cors import CORS
from flask_pymongo import PyMongo
from ....ISEAR_app import ISEAR_app

try:
    from .....settings import BASE_DIR
except:
    from settings import BASE_DIR

# Load Config File for DB
ISEAR_app.config.from_pyfile(BASE_DIR+'/app/ISEAR_app/configs/config.cfg')
CORS(ISEAR_app)
mongo = PyMongo(ISEAR_app)

    