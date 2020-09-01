import numpy as np
import pandas as pd 
import re
import nltk
#import spacy
from string import punctuation 
from nltk.stem.porter import PorterStemmer
#from sklearn.externals import joblib
import joblib
import pickle
from sklearn.feature_extraction.text import CountVectorizer


def predict(tweets):
    try:
        model1 = open('model/logistic_regression.pkl','rb')
        model2 = open('model/random_forest.pkl','rb')
        model3 = open('model/decision_tree.pkl','rb')
        clf1 = joblib.load(model1)
        clf2 = joblib.load(model2)
        clf3 = joblib.load(model3)
        
        from nltk.corpus import stopwords
        nltk.download('stopwords')
        nltk.download('wordnet')
        #spc = spacy.load('en')
        stopwords = set(stopwords.words('english')+list(punctuation)+['AT_USER','URL'])

        corpus = []
        for tweet in tweets:    
            tweet = re.sub('[^a-zA-Z]', ' ', tweet)
            tweet = tweet.lower()
            tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
            tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
            #tweet = tweet.split()
            tokenizer = nltk.tokenize.TreebankWordTokenizer()
            tweet = tokenizer.tokenize(tweet)
            #ps = PorterStemmer()
            lmz = nltk.stem.WordNetLemmatizer()
            tweet = [lmz.lemmatize(word) for word in tweet if not word in stopwords ]
            tweet = ' '.join(tweet)
            corpus.append(tweet)

        #data = [tweet]
        cv_model = open('model/count_vectorizer.pkl','rb')
        td_model = open('model/tfidf_vectorizer.pkl','rb')
        cv = joblib.load(cv_model)
        td = joblib.load(td_model)
            
        vect = cv.transform(corpus).toarray()
        vect = td.transform(vect).toarray()
        pred1= clf1.predict(vect)
        pred2= clf2.predict(vect)
        pred3= clf3.predict(vect)

        pred =[]
        for k in range(0,len(pred1)):
            a=[pred1[k],pred1[k],pred1[k],pred2[k],pred3[k]]
            if a.count(0)> a.count(1):
                pred.append(0)
            else:
                pred.append(1)

        return pred

    except:
        return []


