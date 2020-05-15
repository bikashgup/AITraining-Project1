from .data_preprocess import data_preprocessing as DP
from .config import data_paths as Dpath
from .outputs import file_write as FW

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support as PRFS

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

import mlflow
import mlflow.sklearn
from urllib.parse import urlparse



CV = 5
models = [
    LinearSVC(),
    MultinomialNB(),
    LogisticRegression(random_state=0),
]

def plot_confusion_matrix(y_actual, y_pred, model_name, label_encoder):
  cm = confusion_matrix(y_actual, y_pred)
  df_cm = pd.DataFrame(cm, columns = np.unique(label_encoder.inverse_transform(y_actual)), index = np.unique(label_encoder.inverse_transform(y_actual)))
  df_cm.index.name ='Actual'
  df_cm.columns.name = 'Predicted'
  plt.figure(figsize = (10, 8))
  ax = plt.axes()
  sns.set(font_scale =2)
  sns.heatmap(df_cm, cmap = "Blues", ax =ax, annot =True, fmt = "d")
  ax.set_title('Confusion Matrix')
  plt.savefig(Dpath.ISEAR_CONFUSION_MATRIX + model_name+'.png')

  return cm

def save_classification_report(y_train, y_train_pred, y_test, y_test_pred, model):
    print("Training Set")
    print(classification_report(y_train, y_train_pred))

    print("Testing Set")
    print(classification_report(y_test, y_test_pred))
    resultList = [
        'Training set classification report',
        '----------------------------------',
        classification_report(y_train, y_train_pred),
        'Testing set classification report',
        '----------------------------------',
        classification_report(y_test, y_test_pred)
        ]
    FW.write2file(Dpath.ISEAR_CLASSIFICATION_REPORTS + model, resultList)

def main():

    ## getting X, Y dataset
    X, Y, label_encoder = DP.preprocessed_ISEAR_data(Dpath.ISEAR_DATA_PATH)
    entries = []
    ## spltting dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, shuffle=True)
    for model in models:
        with mlflow.start_run(run_name=model.__class__.__name__):
            model_name = model.__class__.__name__
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            precision, recall, f1score, _ = PRFS(y_test, y_test_pred, average="micro")
            mlflow.log_params(model.get_params())
            mlflow.log_metric('accuracy', accuracy_score(y_test, y_test_pred))
            mlflow.log_metrics({'precision':precision, 'recall': recall, 'F1score':f1score})
            mlflow.log_param('classifier', model_name)
            mlflow.log_param('document_term_matrix', 'tidf')
            ## saving classification report for both training and testing set

            save_classification_report(y_train, y_train_pred, y_test, y_test_pred, model_name)
            ## saving images of confusion matrix for testing data
            confusion_matrix = plot_confusion_matrix(y_test_pred, y_test, model_name, label_encoder)

            tracking_url = urlparse(mlflow.get_tracking_uri()).scheme
            # Model registry does not work with file store
            if tracking_url != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name=model_name)
            else:
                mlflow.sklearn.log_model(model, "model")


if __name__ == "__main__":
    main()
