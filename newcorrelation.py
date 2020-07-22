import pandas as pd
import numpy as np
from scipy.stats import pearsonr #import pearsonr to calculate the correlation

tweet_data_df = pd.read_csv("covid19 country metadata.csv") #load processed tweeter data
actual_data_df = pd.read_excel("actualdata.xlsx") #load the actual data

tweet_country = [] #array to store the tweeter country name
for country in tweet_data_df['country name']: #storing the country one by one
    tweet_country.append(country)

#get the actual data on the date 06-07-2020
country_actual_data = actual_data_df.loc[(actual_data_df['day'] == 6) & (actual_data_df['month'] == 7)]

actual_country = [] # store the actual country in array
for country in country_actual_data['countriesAndTerritories']:
        if country in tweet_country:
            actual_country.append(country) #storing the countries one by one

list1_as_set = set(actual_country)
#converting the list to set inorder to find the matching
# countries between actual and tweet countries
intersection = list1_as_set.intersection(tweet_country)

common_country_list = list(intersection)
common_country_list = sorted(common_country_list)
print("country : ",common_country_list) #prints the common county

tweet_count_per_country = [] #array to store the tweet count based on countries
for country in common_country_list:
    data = tweet_data_df.loc[(tweet_data_df['country name'] == country)]
    for value in data['tweet counts']:
        tweet_count_per_country.append(value) #storing the tweet count to the array

print("tweet counts : ",tweet_count_per_country)

confirm_case_per_country = [] #array to store the actual confirm case count based on countries
for country in common_country_list:
    data = country_actual_data.loc[(country_actual_data['countriesAndTerritories'] == country)]
    for value in data['cases']:
        confirm_case_per_country.append(value) #storing the actual confirm case counts

print("confirm cases : ",confirm_case_per_country)

x = pd.Series(tweet_count_per_country) #setting the x parameter to calculate the correlation
y = pd.Series(confirm_case_per_country) #setting the Y parameter to calculate the correlation

correlation = x.corr(y) #calculating the correlation between x and y
print('corelation between tweeter count and confrim case count based on countries on 06-07-2020 : ' , correlation)
