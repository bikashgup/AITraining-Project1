from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import seaborn as sns
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse


import load_data, dtm, evaluate, outputtxt

df = load_data.data_load()
X = dtm.doc_term_matrix(df)
y = df['Emotion']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=42)
top_words = 5000

def train():

    with mlflow.start_run():

        clf = SGDClassifier(loss='hinge', penalty='l2')

        clf.fit(X_train, y_train)
    return clf


def test(clf):
    resultList = clf.predict(X_train)
    model = "SGD-L2"
    outputtxt.write2file("../Output_txtfile/bigram.output.txt", resultList)
    accuracy = evaluate.evaluation(y_train, resultList)
    confusion = evaluate.plot_confusion_matrix(y_train, resultList)
    mlflow.log_param("accuracy", accuracy)
    mlflow.log_param("Classifier", model)

    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

    # Model registry does not work with file store
    if tracking_url_type_store != "file":

        # Register the model
        # There are other ways to use the Model Registry, which depends on the use case,
        # please refer to the doc for more information:
        # https://mlflow.org/docs/latest/model-registry.html#api-workflow
        mlflow.sklearn.log_model(clf, "model", registered_model_name="SGD")
    else:
        mlflow.sklearn.log_model(clf, "model")