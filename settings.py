import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = BASE_DIR + '/ml/data/ISEAR.csv'
AUG_DATA_PATH = BASE_DIR + '/ml/data/augmented_ISEAR.csv'

OUT_PATH = BASE_DIR + '/out/ISEAR/'

CHECKPOINT = BASE_DIR+ '/checkpoints/'

STATIC_IMAGE_PATH = BASE_DIR + '/static/images/'

shared_components = {"db": None}


