from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

import load_data, dtm, evaluate, outputtxt


df = load_data.data_load()
X = dtm.doc_term_matrix(df)
y = df['Emotion']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=42)


def train():

    clf = SGDClassifier(loss='hinge', penalty='l1')
    clf.fit(X_train, y_train)
    return clf

def test(clf):
    resultList = clf.predict(X_test)
    outputtxt.write2file("../Output_txtfile/bigram.output.txt", resultList)
    evaluate.evaluation(resultList, y_test)