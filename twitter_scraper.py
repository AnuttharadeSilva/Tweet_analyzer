from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

# begin_date = dt.date(2020,4,20)
# end_date = dt.date(2020,4,21)

# limit = 5
# lang = 'en'
# keys = "corona"

def stream(keys,begin_date,end_date,limit):
  
  tweets = query_tweets(keys,begindate = begin_date, enddate = end_date,limit =limit, lang ='en')

  df = pd.DataFrame(t.__dict__ for t in tweets )
  df.drop_duplicates(subset = ['text'], keep='first', inplace=True)
  df = df.dropna()
  df = df.reset_index(drop=True)
  data = df['text']
  #print(df)
  
  return data
