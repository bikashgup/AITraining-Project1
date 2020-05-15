from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

def get_document_term_matrix(data):
    '''
    This function:
        -removes the stopwords from sentences in data
        -converts the sentences in data to a matrix of token
         value_counts

    Parameters:
    ---------------
    data: pandas dataframe

    returns:
    --------------
    document_term_matrix: matrix of token
     value_counts
    '''
    vectorizer = CountVectorizer(stop_words='english', ngram_range=(1,2))
    document_term_matrix = vectorizer.fit_transform(data)

    return document_term_matrix

def tfidf(data):
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    document_term_matrix = vectorizer.fit_transform(data)

    return document_term_matrix
