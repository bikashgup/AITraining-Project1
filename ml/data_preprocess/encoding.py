from sklearn.preprocessing import LabelEncoder

def target_encoding(data):
    '''
    This function:
        - uses LabelEncoder() to encode target value

    Parameters:
    -----------
    data: target data from pandas dataframe

    returns:
    --------
    data: encoded data using LabelEncoder
    '''

    le = LabelEncoder()
    data = le.fit_transform(data)

    return data, le
