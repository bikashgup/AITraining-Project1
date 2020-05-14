from data_preprocess import data_preprocessing as DP
from config import data_paths as Dpath
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from outputs import file_write as FW

def main():
    ## getting X, Y dataset
    X, Y = DP.preprocessed_ISEAR_data(Dpath.ISEAR_DATA_PATH)
    ## spltting dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, shuffle=True)
    ## using naive_base classifier
    nb = MultinomialNB()
    nb.fit(X_train, y_train)
    y_train_pred = nb.predict(X_train)
    y_test_pred = nb.predict(X_test)
    print("Training Set")
    print(classification_report(y_train, y_train_pred))

    print("Testing Set")
    print(classification_report(y_test, y_test_pred))
    resultList = [
        classification_report(y_train, y_train_pred),
        classification_report(y_test, y_test_pred)
        ]
    FW.write2file('naive_bayes_result', resultList)


if __name__ == "__main__":
    main()
