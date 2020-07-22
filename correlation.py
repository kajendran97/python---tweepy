import pandas as pd
import numpy as np
from scipy.stats import pearsonr

tweet_data_df = pd.read_csv("covid19 country metadata.csv")

# print(tweet_data_df.head())
# print(tweet_data_df['country name'])


# tweet_count = []
# for count in tweet_data_df['tweet counts']:
#     tweet_count.append(count)
# print(country_name)
# print(tweet_count)

actual_data_df = pd.read_excel("actualdata.xlsx")
# print("data loaded")

country_actual_data = actual_data_df.loc[(actual_data_df['day'] == 6) & (actual_data_df['month'] == 7)]
# print(country_actual_data['cases'])

actual_country = []

for country in country_actual_data['countriesAndTerritories']:
        actual_country.append(country)

print(actual_country)

for name in actual_country:
    tweet_data_df

# tweet_country_name = []
# for name in tweet_data_df['country name']:
#     if name in actual_country:
#         tweet_country_name.append(name)
#
# print(tweet_country_name)

print(tweet_data_df)

for count in tweet_data_df:
    print(count)













































# country_name = "Australia"
# country_tweeter_data = tweet_data_df.loc[[country_name]]
# country_tweeter_count = country_tweeter_data.size

# country_actual_data = actual_data_df.loc[(actual_data_df['day'] == 6) & (actual_data_df['month'] == 7)]
# country_actual_confirmed_Count = 0
# country_actual_confirmed_Count = int(country_actual_data['cases'])
#
# print(country_name,' tweet count : ',country_tweeter_count)
# print(country_name,' confirm count : ', country_actual_confirmed_Count)
# print(country_actual_data.size)
# x = pd.Series([country_tweeter_count,0])
# y = pd.Series([country_actual_confirmed_Count,0])

# correlation = x.corr(y)
# print('corelation : ' , correlation)
