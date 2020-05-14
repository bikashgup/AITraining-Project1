from sklearn.feature_extraction.text import CountVectorizer
import datacleaning

def doc_term_matrix(data):
    """
     Computes Document Term Matrix.

     Parameters
     ----------
     data : pandas.core.frame.DataFrame
         dataset

     Returns
     -------
     dtm : scipy.sparse.csr.csr_matrix
         sparse document term matrix

     """

    data['Text_clean'] = data['Text'].apply(lambda x: datacleaning.clean_data(x))
    vectorizer = CountVectorizer(stop_words='english', ngram_range=(1,2))
    dtm = vectorizer.fit_transform(data['Text_clean'])
    return dtm
