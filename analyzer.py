import pandas as pd 
import re
import nltk
from nltk.stem.porter import PorterStemmer
from string import punctuation 
from sklearn.externals import joblib
from sklearn.naive_bayes import GaussianNB
import pickle
from sklearn.feature_extraction.text import CountVectorizer


def predict(tweets):
    model1 = open('model/logisticR.pkl','rb')
    #model2 = open('model/SVM.pkl','rb')
    #model3 = open('model/kernelSVM.pkl','rb')
    model4 = open('model/randomF.pkl','rb')
    model5 = open('model/dTree.pkl','rb')
    clf1 = joblib.load(model1)
    #clf2 = joblib.load(model2)
    #clf3 = joblib.load(model3)
    clf4 = joblib.load(model4)
    clf5 = joblib.load(model5)
    
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    stopwords = set(stopwords.words('english')+list(punctuation)+['AT_USER','URL'])
    corpus=[]
    for tweet in tweets:
        tweet = re.sub('[^a-zA-Z]', ' ', tweet)
        tweet = tweet.lower()
        tweet = tweet.split()
        ps = PorterStemmer()
        tweet = [ps.stem(word) for word in tweet if not word in stopwords ]
        tweet = ' '.join(tweet)
        corpus.append(tweet)

    #data = [tweet]
    cv_model = open('model/countV.pkl','rb')
    td_model = open('model/tfidf.pkl','rb')
    cv = joblib.load(cv_model)
    td = joblib.load(td_model)
		
    vect = cv.transform(corpus).toarray()
    vect = td.transform(vect).toarray()
    pred1= clf1.predict(vect)
    #pred2= clf2.predict(vect)
    #pred3= clf3.predict(vect)
    pred4= clf4.predict(vect)
    pred5= clf5.predict(vect)

    pred =[]
    for k in range(0,len(pred1)):
        a=[pred1[k],pred4[k],pred5[k]]
        if a.count(0)> a.count(1):
            pred.append(0)
        else:
            pred.append(1)

    return pred1

