import pandas as pd

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

    return target_labels, data
