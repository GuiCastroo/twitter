"""
Module for config credential of twitter
"""
import twitter


def token(token, token_secret, consumer_key, consumer_secret):
    """
     Functions for create access for Twitter API.

    :param token:
    :param token_secret:
    :param consumer_key:
    :param consumer_secret:
    :return:

    """
    return twitter.Twitter(auth=twitter.OAuth(token, token_secret, consumer_key, consumer_secret))


