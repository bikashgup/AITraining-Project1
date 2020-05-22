import mlflow
import mlflow.sklearn
from urllib.parse import urlparse

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support as PRFS

from ..outputs import (
    save_experiment_reports as SER, 
    save_experiment_outputs_plot as SEOP
)
from ...settings import CHECKPOINT
from ...utils.create_folder import create_folder
from ..model_selection import split_dataset as SD
from ..data_preprocess import data_preprocessing as DP

import joblib

def saving_checkpoints(filepath, data, experiment_name):
    create_folder(CHECKPOINT+experiment_name)
    with open(filepath,'wb') as outputFile:
        joblib.dump(data, outputFile)

def mlflow_saving(params, metrics, support, artifacts, model, experiment_name):
    
    with mlflow.start_run(run_name=model.__class__.__name__+"-"+experiment_name):
        
        mlflow.log_params(params)
        mlflow.log_param('classifier', model.__class__.__name__)
        mlflow.log_metrics(metrics)
        
        if support:
            mlflow.log_metric('support', support)
        
        for i in artifacts:
            mlflow.log_artifact(i)
        
        tracking_url = urlparse(mlflow.get_tracking_uri()).scheme
        # Model registry does not work with file store
        if tracking_url != "file":
            mlflow.sklearn.log_model(model, "model", registered_model_name=model_name)
        else:
            mlflow.sklearn.log_model(model, "model")
        
            


def model_fit(model, test_size, DATA_PATH, OUT_PATH, experiment_name):
    
    ## getting X, Y dataset
    
    X, Y, label_encoder, vectorizer = DP.preprocessed_ISEAR_data(DATA_PATH)
    entries = []
    ## spltting dataset into training and testing sets
    X_train, X_test, y_train, y_test = SD.test_train_split(X, Y, test_size)
    
    model_name = model.__class__.__name__
    model.fit(X_train, y_train)
    
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    # data = vectorizer.inverse_transform(X[0])
    # print(data)
    precision, recall, f1score, support = PRFS(y_test, y_test_pred, average="micro")
    
    ## saving classification report for both training and testing set
    filepath = SER.save_classification_report(
            y_train, y_train_pred, 
            y_test, y_test_pred, model_name, 
            OUT_PATH, experiment_name)
        
    ## saving images of confusion matrix for testing data
    confusion_matrix_train, image_path_testing = SEOP.plot_confusion_matrix(
            y_test_pred, y_test,
            model_name, label_encoder, 
            OUT_PATH, experiment_name, 'testing')
        
    ## saving images of confusion matrix for training data
    confusion_matrix_test, image_path_training = SEOP.plot_confusion_matrix(
            y_train_pred, y_train,
            model_name, label_encoder, 
            OUT_PATH, experiment_name, 'training')
    
    metrics = {
        'precision': precision,
        'recall': recall,
        'f1score': f1score,
        'accuracy': accuracy_score(y_test, y_test_pred),
    }
    artifacts = [filepath, image_path_testing, image_path_training]
    
    mlflow_saving(
        model.get_params(),
        metrics,
        support,
        artifacts,
        model,
        experiment_name
    )    
    ## saving model checkpoints
    saving_checkpoints(CHECKPOINT+experiment_name+'/'+'model', model, experiment_name)
    ## saving Vectorizer checkpoint
    saving_checkpoints(CHECKPOINT+experiment_name+'/'+'vectorizer', vectorizer, experiment_name)
    ## saving metrics checkpoint 
    saving_checkpoints(CHECKPOINT+experiment_name+'/'+'metrics', metrics, experiment_name)
    ## saving label encoder checkpoint 
    saving_checkpoints(CHECKPOINT+experiment_name+'/'+'label_encoder', label_encoder, experiment_name)


    return metrics, support, accuracy_score(y_train, y_train_pred), artifacts