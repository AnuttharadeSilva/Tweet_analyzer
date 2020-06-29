import pandas as pd 
import re
import nltk
import spacy
from string import punctuation 
#from sklearn.externals import joblib
import joblib
from sklearn.naive_bayes import GaussianNB
import pickle
from sklearn.feature_extraction.text import CountVectorizer


def predict(tweets):
#try:
    model1 = open('model/lr_new.pkl','rb')
    model2 = open('model/rf_new.pkl','rb')
    model3 = open('model/dt_new.pkl','rb')
    clf1 = joblib.load(model1)
    clf2 = joblib.load(model2)
    clf3 = joblib.load(model3)
    
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    spc = spacy.load('en')
    stopwords = set(stopwords.words('english')+list(punctuation)+['AT_USER','URL'])

    corpus = []
    for tweet in tweets:    
        tweet = re.sub('[^a-zA-Z]', ' ', tweet)
        tweet = tweet.lower()
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
        doc = spc(tweet)
        tweet = [word.lemma_ for word in doc if not word in stopwords ]
        tweet = ' '.join(tweet)
        corpus.append(tweet)

    #data = [tweet]
    cv_model = open('model/cv_new.pkl','rb')
    td_model = open('model/td_new.pkl','rb')
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

#except:
    #return []


