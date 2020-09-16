"""
Module for user segmentation
"""
import pandas as pd
import numpy as np
df = pd.read_csv('test.csv')
df_user = df[
    ['user_id', 'user_favourites_count', 'user_followers_count', 'user_statuses_count',  'user_location', 'user_name']
]
df_user = df_user.drop_duplicates()
df_group_by_user = df.groupby('user_id').agg({'like_count': np.mean, 'retweet_count': np.mean})
