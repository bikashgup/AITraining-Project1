import pandas as pd

def data_load():

    '''

    Loads the emotion dataset.

    '''

    df = pd.read_csv('../data/ISEAR.csv', names=['S.N', 'Emotion', 'Text'])
    df.drop(['S.N'], axis =1)
    return df