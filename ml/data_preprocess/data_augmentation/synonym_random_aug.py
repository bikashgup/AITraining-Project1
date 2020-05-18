import nlpaug.augmenter.word as naw
import nltk
from nlpaug.util import Action
import pandas as pd


aug_syn = naw.SynonymAug(aug_src='wordnet')
aug_ran = naw.RandomWordAug(action='swap')

def new_data_frame(data):
    df = {'labels':[], 'sentences':[]}
    df = pd.DataFrame(df)
    print(df)
    for i in range(len(data)):
        if data['sentences'][i].find("\n") > 0:
            sentences = data['sentences'][i].replace("\n", " ")
            augmented_sent = aug_syn.augment(sentences)
            df = df.append({'labels':data['labels'][i], 'sentences':augmented_sent}, ignore_index= True)
            augmented_sent = aug_ran.augment(sentences)
            df = df.append({'labels':data['labels'][i], 'sentences':augmented_sent}, ignore_index= True)
        else:
            augmented_sent = aug_syn.augment(sentences)
            df = df.append({'labels':data['labels'][i], 'sentences':augmented_sent}, ignore_index= True)
            augmented_sent = aug_ran.augment(sentences)
            df = df.append({'labels':data['labels'][i], 'sentences':augmented_sent}, ignore_index= True)
    new_df =  pd.concat([data, df], ignore_index=True) 
    
    print(data.shape, df.shape, new_df.shape, "hello")
    return new_df  

