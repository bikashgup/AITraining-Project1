from ....ISEAR_app import ISEAR_app
from flask import request, render_template
from .....settings import shared_components, BASE_DIR
from ..models.models import mongo
from datetime import datetime as dt
from ...config import CHECKPOINT
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd
import joblib

# Select the database
db = mongo.db
shared_components['db'] = db


def read_file(filepath):
    with open(filepath, 'rb') as fp:
        action = joblib.load(fp)
    return action

model = read_file(CHECKPOINT + 'experiment2/model')
label_encoder = read_file(CHECKPOINT+ 'experiment2/label_encoder')
vectorizer = read_file(CHECKPOINT + 'experiment2/vectorizer')
metrics = read_file(CHECKPOINT + 'experiment2/metrics')

@ISEAR_app.route('/')
def index():
    data = {
        'metrics':metrics,
        'model': model.__class__.__name__
    }
    return render_template('index.html', data=data)

@ISEAR_app.route('/save_model_result', methods=['POST'])
def save_model_result():
    if request.method == 'POST':
        precision = request.form['precision']
        accuracy = request.form['accuracy']
        recall = request.form['recall']
        f1score = request.form['f1score']
        model_name = request.form['model']        
        data = {
            'precision': precision,
            'accuracy': accuracy,
            'model': model_name,
            'recall': recall,
            'f1score': f1score
        }
        print(data)

        database = shared_components['db']

        database.model_result.insert(data)
        
        
        return render_template('index.html', data = {'metrics':metrics, 'model':model_name, 'success_text':'Your model saved succefuuly.'} )
    
