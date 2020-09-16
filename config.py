"""
Module for config credential of twitter
"""
import twitter
import os
import tweepy


def token():
    """ Functions for create access for Twitter API. """
    auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
    auth.set_access_token(os.environ['token'], os.environ['token_secret'])
    return tweepy.API(auth, wait_on_rate_limit=True)


