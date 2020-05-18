from . import document_term_matrix as DTM
from . import encoding as DEncode

from ..data_cleaning import cleaning_data as cleanD
from ..data_cleaning import data_loading as loadD
from .data_augmentation import synonym_random_aug as SR_AUG
import os 

save_path = os.path.dirname(os.path.dirname(__file__)) + '/data/augmented_ISEAR.csv'

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
    target_labels, data = loadD.loading_augmented_ISEAR_data(path)
    
    ## cleaning data
    data['sentences'] = data['sentences'].apply(lambda x:cleanD.cleaning_ISEAR_data(x))
    
    ## getting the document_term_matrix
    # dtm = DTM.get_document_term_matrix(data['sentences'])
    
    dtm = DTM.tfidf(data['sentences'])
    
    ## label encoding target data
    Y, label_encoder = DEncode.target_encoding(data['labels'])

    return dtm, Y, label_encoder

def saving_augmented_data(data):
    
    data = SR_AUG.new_data_frame(data)
    data.to_csv(save_path)
    