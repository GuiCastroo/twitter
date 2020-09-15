"""
Module for interact with twitter
"""

import pprint
import os
from config import token

API = token(
    token=os.environ['token'], token_secret=os.environ['token_secret'],
    consumer_key=os.environ['consumer_key'],
    consumer_secret=os.environ['consumer_secret']
)

tweets = API.search.tweets(q="#pycon")
