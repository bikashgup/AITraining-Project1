from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

def test_train_split(X, Y, test_size):
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, shuffle=True)

    return X_train, X_test, y_train, y_test
    