import nlpaug.augmenter.word as naw
import nltk
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nlpaug.util import Action
import pandas as pd

aug_syn = naw.SynonymAug(aug_src='wordnet')
aug_ran = naw.RandomWordAug(action='swap')


def new_data_frame(data):
    df = {'Text': [], 'Emotion': []}
    df = pd.DataFrame(df)
    print(df)
    for i in range(len(data)):
        if data['Text'][i].find("\n") > 0:
            sentences = data['Text'][i].replace("\n", " ")
            augmented_sent = aug_syn.augment(sentences)
            df = df.append({'Emotion': data['Emotion'][i], 'Text': augmented_sent}, ignore_index=True)
            augmented_sent = aug_ran.augment(sentences)
            df = df.append({'Emotion': data['Emotion'][i], 'Text': augmented_sent}, ignore_index=True)
        else:
            augmented_sent = aug_syn.augment(sentences)
            df = df.append({'Emotion': data['Emotion'][i], 'Text': augmented_sent}, ignore_index=True)
            augmented_sent = aug_ran.augment(sentences)
            df = df.append({'Emotion': data['Emotion'][i], 'Text': augmented_sent}, ignore_index=True)
    new_df = pd.concat([data, df], ignore_index=True)

    print(data.shape, df.shape, new_df.shape, "hello")
    # new_df.drop(['S.N'], axis=1, inplace = True)
    return new_df