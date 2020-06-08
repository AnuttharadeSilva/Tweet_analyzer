from flask import Flask, request, redirect, url_for, jsonify, render_template
from flask_bootstrap import Bootstrap
from datetime import date
#import timeit

import analyzer
#import twitter_scraper
import tweepy_streamer

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        key1 = request.form['key1']
        key2 = request.form['key2']
        limit = int(request.form['limit'])
        begin = request.form['begindate']
        end= request.form['enddate']

        keys = " AND ".join([key1,key2])
        begin_date = date(*map(int, begin.split('-')))
        end_date = date(*map(int, end.split('-')))

        #start_time = timeit.default_timer()
        #tweets = twitter_scraper.stream(keys,begin_date,end_date,limit)
        tweets = tweepy_streamer.get_tweets(keys,begin_date,end_date,limit)
        #print("time: ",timeit.default_timer() - start_time)

        if len(tweets)>0:
            result = analyzer.predict(tweets)
            #result = result.tolist()
            percent = [(result.count(0))/len(result)*100 , (result.count(1))/len(result)*100]

            return jsonify({'percent' : percent, 'tweets' : tweets.tolist(), 'predictions' : result})
            #return render_template('show.html',result=result,tweets=tweets,number=len(tweets),percent=percent)
        else:
            return jsonify({'percent' : None, 'tweets' : None, 'predictions' : None})

    return render_template('index.html')
    #return jsonify({'message' : 'A POST request is required. GET request recieved!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)