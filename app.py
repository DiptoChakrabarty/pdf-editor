from dotenv import load_env()
load_env()

access_key = os.environ["API_KEY"]
secret_key = os.environ["API_SECRET_KEY"]
consumer_token = os.environ["COSUMER_TOKEN"]
consumer_secret = os.environ["COSUMER_SECRET"]



import json
from tweepy.streaming import StreamListener
from  tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch
