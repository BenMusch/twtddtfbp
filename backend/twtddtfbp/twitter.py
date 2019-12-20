import os

import tweepy


consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET']
accesss_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

username = 'meganamram'

def get_tweets_by_id(tweet_ids):
    api.statuses_lookup(tweet_ids)

def get_tweets_until_id(until_id):
    api.user_timeline(username, until_id)
