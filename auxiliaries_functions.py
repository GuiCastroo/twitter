from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd


def definition_gender_by_name(name):
    """ Definer gender from name. """

    data_frame_name = pd.read_csv("nomes.csv")
    choice = data_frame_name.first_name.to_list()
    similar = process.extract(name, choice, limit=10)
    similar = [names[0] for names in similar]
    gender = data_frame_name.query(f'first_name in {similar}').groupby('classification').size().to_dict()

    return {'name': name, 'gender': max(gender)}


def add_gender_for_df_by_user_or_followers(df):
    df['gender'] = df['user_name'].apply(lambda name: definition_gender_by_name(name)['gender'])
    return df

df = pd.read_csv('df_followers_orlando.csv',  sep=";")
new_df = add_gender_for_df_by_user_or_followers(df)
