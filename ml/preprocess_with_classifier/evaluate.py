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
    # print("Confusion Matrix:\n", confusion_matrix(y_actual, y_test))
    accuracy = accuracy_score(y_actual, y_test)
    confusion = confusion_matrix(y_actual, y_test)
    print("THe accuracy of SGD Classifier is: ", accuracy_score(y_actual, y_test))
    return accuracy

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

def plot_classification_report(cr, title='Classification report ', with_avg_total=False, cmap=plt.cm.Blues):

    lines = cr.split('\n')

    classes = []
    plotMat = []
    for line in lines[2 : (len(lines) - 3)]:
        #print(line)
        t = line.split()
        # print(t)
        classes.append(t[0])
        v = [float(x) for x in t[1: len(t) - 1]]
        print(v)
        plotMat.append(v)

    if with_avg_total:
        aveTotal = lines[len(lines) - 1].split()
        classes.append('avg/total')
        vAveTotal = [float(x) for x in t[1:len(aveTotal) - 1]]
        plotMat.append(vAveTotal)


    plt.imshow(plotMat, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    x_tick_marks = np.arange(3)
    y_tick_marks = np.arange(len(classes))
    plt.xticks(x_tick_marks, ['precision', 'recall', 'f1-score'], rotation=45)
    plt.yticks(y_tick_marks, classes)
    plt.tight_layout()
    plt.ylabel('Classes')
    plt.xlabel('Measures')