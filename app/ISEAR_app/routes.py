import joblib
import matplotlib.pyplot as plt
import numpy as np
from flask import url_for
from .run_app import run_app
from flask import request, render_template
from .settings import shared_components, BASE_DIR
from .models import mongo
from datetime import datetime as dt
from .config import CHECKPOINT
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

@run_app.route('/')
def index():
    data = {
        'metrics':metrics,
        'model': model.__class__.__name__
    }
    return render_template('index.html', data=data)

@run_app.route('/save_model_result', methods=['POST'])
def save_model_result():
    if request.method == 'POST':
        precision = request.form['precision']
        accuracy = request.form['accuracy']
        recall =  request.form['recall']
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
    
@run_app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html', data={'model':model.__class__.__name__})
    elif request.method == 'POST':
        data = request.form['data']
        text = data
        data = data.lower()
        data = vectorizer.transform([data,])
        print(data)
        y = model.predict(data)
        proba = model.predict_proba(data)
        
        predicted_value = label_encoder.inverse_transform(y)
        classes = label_encoder.classes_
        y_pos = np.arange(len(classes))
        print(classes, predicted_value, proba)
        plt.figure(figsize = (10, 8))
        plt.barh(y_pos, proba[0], align='center')
        plt.yticks(y_pos, tuple(classes))
        plt.xlabel('predict_proba')
        data = {
            'model':model.__class__.__name__,
            'predicted_value': predicted_value[0],
            'filepath': '/images/image.png',
            'datetime': dt.now()
        }
        database = shared_components['db']
        database.predicted_output.insert(data)
        filepath = BASE_DIR + '/static/images/'
        plt.savefig(filepath +'image.png')
        data['success_text'] = 'predictted your output'
        data['text'] = text

        return render_template('predict.html', data=data)
