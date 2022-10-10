import json
import numpy as np
import random

import pickle

import nltk
#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("language.json").read())

words=pickle.load(open('words.pkl','rb'))
classes=pickle.load(open('classes.pkl','rb'))

model=load_model('chatbot_model.h5')

def clean_input(phrase):
    phrase_words = nltk.word_tokenize(phrase)
    phrase_words=[lemmatizer.lemmatize(word)for word in phrase_words]
    return phrase_words

def bag_of_words(phrase):
    phrase_words=clean_input(phrase)
    bag= [0] * len(words)
    for w in phrase_words:
        for i,word in enumerate(words):
            if word ==  w:
                bag[i]=1
    return np.array(bag)

def predict_class(phrase):
    b_o_w=bag_of_words(phrase)
    res=model.predict(np.array([b_o_w]))[0]
    ERROR_TRESHOLD=0.25
    results=[[i,r] for i,r in enumerate(res) if r>ERROR_TRESHOLD]
    results.sort(key=lambda x:x[1],reverse=True)
    return_list=[]
    for r in results:
        return_list.append({'intent':classes[r[0]],'probability':str(r[1])})
    return return_list
