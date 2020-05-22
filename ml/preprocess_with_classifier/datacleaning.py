import string
import random
import pandas as pd




def clean_data(txt):
    """
    Remove punctuations from the text.

    Parameters
#     ----------
    txt : str
        all strings of the dataframe

    Returns
    -------
    txt : str
        string without punctuation

    """

    txt = "".join([c for c in txt if c not in string.punctuation])
    return txt



