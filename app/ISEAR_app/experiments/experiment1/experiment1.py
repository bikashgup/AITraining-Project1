from sklearn.naive_bayes import MultinomialNB
 
from ...config import DATA_PATH, OUT_PATH
from ....ml.model_selection import model_selection as MS

test_size = 0.2
experiment_name = 'experiment1/1.0'

def experiment1():
   
   nb = MultinomialNB()
   mertrics, training_score, artifacts = MS.model_fit(nb, test_size, DATA_PATH, OUT_PATH, experiment_name)