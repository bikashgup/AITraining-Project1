from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

def evaluation(y_actual, y_test):

    """
    This evaluates the classifier with confusion matrix and accuracy.

    """
    print("Confusion Matrix:\n", confusion_matrix(y_actual, y_test))
    print("THe accuracy of SGD Classifier is: ", accuracy_score(y_actual, y_test))