from tweepy import API
from tweepy import Cursor
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials
import pandas as pd


def authenticate_twitter_app():
    auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
    auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
    return auth

def get_api():
    api = API(authenticate_twitter_app(),wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

def get_tweets(search_items, begin_date, end_date, num_tweets):
    tweets = []
    for tweet in Cursor(get_api().search, q=search_items,lang="en", since=begin_date ,until=end_date ,result_type="recent").items(num_tweets):
        tweets.append(tweet)
        
    df = pd.DataFrame(data= [tweet.text for tweet in tweets], columns = ['tweets'])
    df.drop_duplicates(subset = ['tweets'], keep='first', inplace=True)
    df = df.dropna()
    df = df.reset_index(drop=True)
    tweets = df['tweets']

    return tweets.tolist()





