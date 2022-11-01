# Tweet Analyzer

This repository contain source code for tweet analyzing tool created using Flask and Twitter API

## Directory Structure

The important files and directories of the repository

    ├── app.py : flask app
    ├── analyzer.py : predict result using NLP models
    ├── twitter_scraper.py : scrape realtime tweets using twitter API
    ├── tweepy_streamer.py : scrape realtime tweets using tweepy library
    ├── test.py : unit testing
    ├── model :
        ├── NLP models (in .pkl format) 
    ├── templates :                  
        ├── index.html
        ├── show.html
        ├── base.html
        
The source code of the trained models can be found [here](https://github.com/AnuttharadeSilva/t_analyzer_model)

## Getting started

Run these commands in terminal/command promt:

```commandline
git clone https://github.com/AnuttharadeSilva/t_analyzer
cd t_analyzer
py -3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask run
```
Navigate to http://localhost:5000/


# Sentiment analysis models

https://github.com/AnuttharadeSilva/tweet_analyzer_model

