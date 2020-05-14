import string

def cleaning_ISEAR_data(data):
    """
     This function:
        -cleans data of its punctuation
        -convert uppper case into lowercase

    Parameters
    ---------------
    data - sentence list

    returns
    ---------------
    data - sentences

    """
    ## removing the puntuation like ',', '.', from the sentences
    ## and combining them
    data = "".join(txt for txt in data if txt not in string.punctuation)

    ## converting data into lowercase
    data = data.lower()

    return data
