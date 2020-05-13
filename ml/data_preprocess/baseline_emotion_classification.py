##Importing Libraries
import pandas as pd
import string
import csv
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


##Loading Dataset
df = pd.read_csv('ISEAR.csv', names=['S.N','Emotion','Text'])
df.drop(['S.N'], axis =1)


def clean_data(txt):
    """
    Remove punctuations from the text.

    Parameters
    ----------
    txt : str
        all strings of the dataframe

    Returns
    -------
    txt : str
        string without punctuation

    """

    txt = "".join([c for c in txt if c not in string.punctuation])
    return txt


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

    df['Text_clean'] = df['Text'].apply(lambda x: clean_data(x))
    vectorizer = CountVectorizer(stop_words='english', ngram_range=(1,2))
    dtm = vectorizer.fit_transform(data['Text_clean'])
    return dtm



def write2file(filename,resultList):
    """
    Writes the output class to the txt file.

    Parameters
    ----------
    filename : str
        Output file name.
    resultList :
        Actual output of the test set from the trained classifier.

    Returns
    -------
    None
    """
    with open(filename,'w',newline='') as outputFile:
        writer = csv.writer(outputFile)
        for result in resultList:
            writer.writerow([result])


def evaluate(y_actual, y_test):

    """
    This evaluates the classifier with confusion matrix and accuracy.

    """
    print(confusion_matrix(y_actual, y_test))
    print(accuracy_score(y_actual, y_test))


def main():

    clf = SGDClassifier(loss='hinge', penalty='l1') ## Stochastic Gradient CLassifier

    X = doc_term_matrix(df)
    y = df['Emotion']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
    clf.fit(X_train, y_train)

    resultList = clf.predict(X_test)
    write2file("bigram.output.txt", resultList)


if __name__ == "__main__":
    main()