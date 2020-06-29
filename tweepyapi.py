from tweepy import API
from tweepy import Cursor
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials
import numpy as np
import pandas as pd
import analyzer


class TwitterClient():
    def __init__(self): 
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_tweets(self, num_tweets, search_items):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=search_items,lang="en").items(num_tweets):
            tweets.append(tweet)
        return tweets



class TwitterAuthenticator():
    def authenticate_twitter_app(self): #class method
        auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
        auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
        return auth


class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        #This handles twitter authentication and connection to the twitter streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app() 
        stream = Stream(auth, listener)
        stream.filter(track= hash_tag_list)



class TwitterListener(StreamListener):
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename     

    def on_data(self,data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data) #append data to json file
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True

    def on_error(self,status): #when rate limit occurs 
        if status == 420:
            return False
        print(status)


class TweetAnalyzer():
    def tweets_to_data_frame(self,tweets):
        df = pd.DataFrame(data= [tweet.text for tweet in tweets], columns = ['Tweets'])
        return df


if __name__ == "__main__":
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    keyword = input("Enter keyword: ").split()
    num_tweets = int(input("Enter no: "))
    search_items = " AND ".join(keyword)

    tweets = twitter_client.get_tweets(num_tweets,search_items)
    df = tweet_analyzer.tweets_to_data_frame(tweets)
    pred = analyzer.predict(df['Tweets'])

    print(pred)








