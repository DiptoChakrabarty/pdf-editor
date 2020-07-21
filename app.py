import json
from tweepy.streaming import StreamListener
from  tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch
from dotenv import load_env()
load_env()


# load env values
access_key = os.environ["API_KEY"]
secret_key = os.environ["API_SECRET_KEY"]
consumer_token = os.environ["COSUMER_TOKEN"]
consumer_secret = os.environ["COSUMER_SECRET"]

el = Elasticsearch()

class tweetlistener(StreamListener):

    def data_load(self,data):

        #decode json
        dict_data = json.loads(data)

        #pass a tweet into the TextBlob Object
        tweet = TextBlob(dict_data["text"])

        #check polarity
        polarity = tweet.sentiment.polarity
        subjectivity = tweet.sentiment.subjectivity

        if polarity < 0:
            sentiment = "negative"
        elif polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        ## add data to elasticsearch

        el.index(index="sentiment",
                doc_type="test-type",
                body={"author": dict_data["user"]["screen_name"],
                "date": dict_data["created_at"],
                "message": dict_data["text"],
                "polarity": polarity,
                "subjectivity": subjectivity,
                "sentiment": sentiment
                })
        return True
    
    def on_erro(self,status):
        print(status)


if __name__ == "__main__":

    listener = TweetStreamListener()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth,listener)

    stream.filter(track=['amazon'])





