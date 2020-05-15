import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ..config import data_paths as Dpath

def loading_ISEAR_data(path):
    '''
        This function:
            -loads the data

        Parameters:
        --------------
        path: data_path

        returns:
        ----------------
        data: pandas dataframe
        target_labels: target_labels
    '''
    print(path)

    data = pd.read_csv(path, header=None)
    print(data.head())

    data.drop(columns=[0], inplace=True)
    target_labels = data[1].value_counts().keys().tolist()
    print(target_labels)
    data[1] = data[1].astype('category')
    ## adding the column containing numerical representatipn of emotion in column 1
    data[3] = data[1].cat.codes
    ## sorting the dataframe according to product id
    data = data.sort_values(3)
    ## countplot for emotion column i.e column 1 in dataframe
    fig, ax1 = plt.subplots(figsize=(10,5))
    plot = sns.countplot(x=1, data=data)
    plt.xlabel('Emotion category')
    plt.ylabel('frequecy')
    plt.title('Emotion Category vs Number of particular emotion data ')
    plt.savefig(Dpath.ISEAR_VISUALIZE + 'Emotion_category_Counts.png')


    return target_labels, data
