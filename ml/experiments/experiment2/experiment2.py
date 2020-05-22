from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
try:
   from settings import AUG_DATA_PATH, OUT_PATH
except:
   from ....settings import AUG_DATA_PATH, OUT_PATH
from ...model_selection import model_selection as MS

test_size = 0.2
experiment_name = 'experiment2/5.0'
models = [
    MultinomialNB(),
    LinearSVC(),
    LogisticRegression(random_state=0),
]

def experiment1():
   
   nb = MultinomialNB()
   mertrics, support, training_score, artifacts = MS.model_fit(nb, test_size, AUG_DATA_PATH, OUT_PATH, experiment_name)
   
def experiment2():
   for model in models:    
      mertrics, support, training_score, artifacts = MS.model_fit(model, test_size, AUG_DATA_PATH, OUT_PATH, experiment_name)