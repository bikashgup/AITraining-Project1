from sklearn.metrics import classification_report

from . import file_write as FW
try:
    from utils import create_folder
except:
    from ...utils import create_folder


def save_classification_report(y_train, y_train_pred, y_test, y_test_pred, model, OUT_PATH, experiment_name):
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
    filepath = OUT_PATH+ experiment_name + '/reports/classifcation_reports/'
    create_folder.create_folder(filepath)
    FW.write2file(filepath + model, resultList)
    
    return filepath + model