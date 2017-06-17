#!/usr/bin/env python
#
import os
from datetime import datetime
import tweepy

consumer_key    = os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
access_key      = os.environ["TWITTER_ACCESS_KEY"]
access_secret   = os.environ["TWITTER_ACCESS_SECRET"]

def timestamp(fmt='%Y-%m-%d %H-%M-%S'):
    return datetime.now().strftime(fmt)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api  = tweepy.API(auth)

# This tweets, so all your followers will see it.
#api.update_status('ANOTHER TEST from python script sent using #tweepy')


# This sends a direct message so only the user "@twiliotest" will see it.
# If @twiliotest does not follow you the message won't go through.
# So if you don't want to set up a separate twitter account then you should
# follow @twiliotest and it will automatically follow you back.
api.send_direct_message(user='@twiliotest', text='Hello from Python! ' + timestamp())
exit(0)

