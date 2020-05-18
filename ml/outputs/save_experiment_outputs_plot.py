import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

from ...utils import create_folder

def plot_confusion_matrix(y_actual, y_pred, model_name, label_encoder, OUT_PATH, experiment_name, set_name):
    '''
        This function: 
            - plot the confusion matrix
            - save the data in the file
            
        Parameters:
        -----------
        y_actual: <numpy.ndarray>-acutal target value
        y_pred: <numpy.ndarray>-predicted target value
        model_name: <string>-model used for experiment
        label_encoder: instance of LabelEncoder() 
        experiment_name: <string>
        
        return:
        -------
        cm: confusion matrix
        
    '''
    print(type(y_actual), type(y_pred))
    cm = confusion_matrix(y_actual, y_pred)
    df_cm = pd.DataFrame(cm, columns = np.unique(label_encoder.inverse_transform(y_actual)), index = np.unique(label_encoder.inverse_transform(y_actual)))
    df_cm.index.name ='Actual'
    df_cm.columns.name = 'Predicted'
    plt.figure(figsize = (10, 8))
    ax = plt.axes()
    sns.set(font_scale =2)
    sns.heatmap(df_cm, cmap = "Blues", ax =ax, annot =True, fmt = "d")
    ax.set_title('Confusion Matrix')
    filepath =  OUT_PATH + experiment_name + '/confusion_matrix/' + set_name + '/'
    create_folder.create_folder(filepath)
    plt.savefig(filepath + model_name+'.png')
    
    return cm, filepath + model_name + '.png'