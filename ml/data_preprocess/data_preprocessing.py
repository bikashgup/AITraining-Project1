from . import document_term_matrix as DTM
from . import encoding as DEncode

from ..data_cleaning import cleaning_data as cleanD
from ..data_cleaning import data_loading as loadD


def preprocessed_ISEAR_data(path):
    '''
    This function:
        - proprocesses the ISEAR data

    Parameters:
    -----------
    path: data location

    Returns:
    --------
    dtm : document_term_matrix of the ISEAR data containig text
    Y   : encoded target labels
    '''

    ## getting target_labels and data
    target_labels, data = loadD.loading_ISEAR_data(path)
    ## cleaning data
    data[2] = data[2].apply(lambda x:cleanD.cleaning_ISEAR_data(x))
    ## getting the document_term_matrix
    #dtm = DTM.get_document_term_matrix(data[2])
    dtm = DTM.tfidf(data[2])
    ## label encoding target data
    Y, label_encoder = DEncode.target_encoding(data[1])

    return dtm, Y, label_encoder
