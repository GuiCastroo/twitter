"""
Module for interact with twitter
"""
from typing import Dict, Any, Union
import pandas as pd
from config import token, tweepy
import logging
from scipy.spatial import distance
import time

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


def get_followers_from_user(user_name):
    """

    :param user_name: name of user that you want to get a list of followers users
    :type user_name: str
    :return: list os followers users
    :rtype: list

    """
    list_of_users = list()
    list_of_users_stage = list()
    for page in tweepy.Cursor(API.followers, screen_name=user_name).pages():
        print('entrou no get')
        print(page)
        list_of_users_stage.append(page)
        print('saiu do get')
        for user in list_of_users_stage[0]:
            print('montando dict')
            user_features = {
                'user_id': user.id,
                'user_followers_count': user.followers_count,
                'user_name': user.name,
                'user_screen_name': user.screen_name,
                'user_friends_count': user.friends_count,
                'user_statuses_count': user.statuses_count,
                'user_verified': user.verified,
                'user_location': user.location,
                'user_favourites_count': user.favourites_count
            }
            list_of_users.append(user_features)
            print('dict pronto')
        time.sleep(60)
    return list_of_users


def get_tweets_by_user(user_id=None, user_name=None):
    """
    :param user_id: user id
    :type user_id: str
    :user_name: user name
    :type user_name: str
    :return: list os followers users
    :rtype: list
    """
    if user_id is None and user_name is None:
        raise AttributeError("You need pass or param user_id or user_name for use function")
    elif user_id is None:
        user_id = API.get_user(user_name).id
    list_of_tweets = list()
    for tweet in tweepy.Cursor(API.user_timeline, user_id=user_id, count=1000).pages():
        for status in tweet:
            format_tweet = {
                'id': status.id,
                'created_at': status.created_at,
                'text': status.text,
                'like_count': status.favorite_count,
                'retweet_count': status.favorite_count,
                'geo': status.geo,
                'user_id': status.user.id,
            }
            list_of_tweets.append(format_tweet)
    return list_of_tweets


def create_csv_for_followers(user_name):
    followers = get_followers_from_user(user_name)
    print('create df')
    df_followers = pd.DataFrame(followers)
    print('create csv')
    df_followers.to_csv(f'{user_name}_followers.csv', sep=';', encoding='UTF-8', index=False)


def create_csv_for_tweets_by_user(user_id=None, user_name=None, name_csv=None):
    tweets = get_tweets_by_user(user_id, user_name)
    print('create df')
    df_tweets = pd.DataFrame(tweets)
    print('create csv')

    if not user_name and not name_csv:
        user_name = API.get_user(user_id).name
    if name_csv:
        csv_name = f'{name_csv}_tweets.csv'
    else:
        csv_name = f'{user_name}_tweets.csv'
    df_tweets.to_csv(csv_name, sep=';', encoding='UTF-8', index=False)


def crate_csv_of_Tweeters_by_followers_of_user(df_name):
    df = pd.read_csv(df_name, sep=';')
    list_of_id = df.user_id.to_list()
    for user_id in list_of_id:
        create_csv_for_tweets_by_user(user_id=user_id)
