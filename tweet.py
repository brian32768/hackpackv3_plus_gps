#!/usr/bin/env python
#
import os, sys
import tweepy

consumer_key    = os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
access_key      = os.environ["TWITTER_ACCESS_KEY"]
access_secret   = os.environ["TWITTER_ACCESS_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

api.update_status('ANOTHER TEST from python script sent using #tweepy')

exit(0)

