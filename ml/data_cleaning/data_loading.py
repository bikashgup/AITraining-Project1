import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
try:
    from settings import BASE_DIR
except:
    from ...settings import BASE_DIR
from utils import create_folder

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

    data = pd.read_csv(path, names=['index', 'labels', 'sentences'])
    print(data.head())

    data.drop(columns=['index'], inplace=True)
    target_labels = data['labels'].value_counts().keys().tolist()
    print(target_labels)

    data['labels'] = data['labels'].astype('category')

    ## adding the column containing numerical representatipn of emotion in column 1

    data['label_id'] = data['labels'].cat.codes

    ## sorting the dataframe according to emotion id i.e column 1

    data = data.sort_values('label_id')

    ## countplot for emotion column i.e column 1 in dataframe

    # fig, ax1 = plt.subplots(figsize=(10,5))
    # plot = sns.countplot(x='labels', data=data)
    # plt.ylabel('frequecy')
    # plt.title('Emotion Category vs Number of particular emotion data ')
    # filepath = BASE_DIR + 'out/ISEAR/data_visualization/'
    # create_folder.create_folder(filepath)
    # plt.savefig( filepath + 'Emotion_category_Counts.png')


    return target_labels, data   


def loading_augmented_ISEAR_data(path):
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

    data = pd.read_csv(path)
    print(data.head())

    target_labels = data['labels'].value_counts().keys().tolist()
    print(target_labels)

    data['labels'] = data['labels'].astype('category')

    # adding the column containing numerical representatipn of emotion in column 1

    data['label_id'] = data['labels'].cat.codes

    # sorting the dataframe according to emotion id i.e column 1

    data = data.sort_values('label_id')

    # countplot for emotion column i.e column 1 in dataframe

    # fig, ax1 = plt.subplots(figsize=(10,5))
    # plot = sns.countplot(x='labels', data=data)
    # plt.xlabel('Emotion category')
    # plt.ylabel('frequecy')
    # plt.title('Emotion Category vs Number of particular emotion data ')
    # filepath = BASE_DIR + '/out/ISEAR/data_visualization/'
    # create_folder.create_folder(filepath)
    # plt.savefig( filepath + 'Augemented_Emotion_category_Counts.png')


    return target_labels, data
