import os
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

### ISEAR

ISEAR_DATA_PATH = BASE_DIR + '/ml/data/ISEAR.csv'

ISEAR_VISUALIZE = BASE_DIR + '/ml/data_visualize/ISEAR/'

ISEAR_OUPUTS  = BASE_DIR + '/ml/outputs/ISEAR/'

ISEAR_CLASSIFICATION_REPORTS = ISEAR_OUPUTS + 'classification_reports/'
ISEAR_CONFUSION_MATRIX = ISEAR_OUPUTS + 'confusion_matrix/'
