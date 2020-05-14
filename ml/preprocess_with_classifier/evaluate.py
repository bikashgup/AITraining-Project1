from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn

def evaluation(y_actual, y_test):

    """
    This evaluates the classifier with confusion matrix and accuracy.

    """
    print("Confusion Matrix:\n", confusion_matrix(y_actual, y_test))
    print("THe accuracy of SGD Classifier is: ", accuracy_score(y_actual, y_test))

def plot_confusion_matrix(y_actual, y_pred):
  data = confusion_matrix(y_actual, y_pred)
  df_cm = pd.DataFrame(data, columns = np.unique(y_actual), index = np.unique(y_actual))
  df_cm.index.name ='Actual'
  df_cm.columns.name = 'Predicted'
  plt.figure(figsize = (10, 8))
  ax = plt.axes()
  sn.set(font_scale =2)
  sn.heatmap(df_cm, cmap = "Blues", ax =ax, annot =True, fmt = "d")
  ax.set_title('Confusion Matrix')
  plt.show()