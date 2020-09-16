"""
Module for interact with twitter
"""
from typing import Dict, Any, Union

from config import token, tweepy
import logging
from scipy.spatial import distance
API = token()


def create_list_of_tweets(str_research, since_date):
    """
    Create a list of all tweets of since_date that you wish.

    :param str_research: name that you wish research
    :type str_research: str
    :param since_date: Date you wish research, since_date most equal the format YYY-MM-DD
    :type since_date: str
    :return: list with all information about of tweets
    :rtype: list

    """
    list_of_tweets = list()
    for tweet in tweepy.Cursor(API.search, q=str_research, count=100, lang="pt", since=since_date).items():
        format_tweet = {
            'id': tweet.id,
            'created_at': tweet.created_at,
            'text': tweet.text,
            'like_count': tweet.favorite_count,
            'retweet_count': tweet.favorite_count,
            'geo': tweet.geo,
            'user_name': tweet.user.name,
            'user_favourites_count': tweet.user.favourites_count,
            'user_followers_count': tweet.user.followers_count,
            'user_friends_count': tweet.user.friends_count,
            'user_statuses_count': tweet.user.statuses_count,
            'user_location': tweet.user.location,
            'user_verified': tweet.user.verified,
            'user_id': tweet.user.id,
        }
        list_of_tweets.append(format_tweet)
    return list_of_tweets


