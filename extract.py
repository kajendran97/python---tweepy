from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pandas as pd
import csv
import re #regular expression
# from textblob import TextBlob
import string
import tweepy

api_key = "HLnOFAqRgkrJaaqMoy41a0nxj" # <---- Add your API Key
api_secret = "tz4GKwFn9dsqYv6Mnl9mzctSqV5LeOVGhAuvr1KW0c2LpLuprZ" # <---- Add your API Secret
access_token = "763929928219766784-AjLCTTzhDWx87EJxHpfeC7IPvFnQB1t" # <---- Add your access token
access_token_secret = "MTJThLdK6SkVzqnHEGvja2yUhIDSCZ8XCfNzjDTUgiXAu" # <---- Add your access token secret

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
hashtag_phrase = "#Covid19"
fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

#open the spreadsheet we will write to
with open('%s.csv' % (fname), 'w', encoding='utf-8') as file:

    w = csv.writer(file)

    #write header row to spreadsheet
    w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count','place'])

    #for each tweet matching our hashtags, write relevant info to the spreadsheet
    for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', \
                                lang="en", tweet_mode='extended', until='2020-07-07').items(2000):
        w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count,tweet.user.location])

print('twitter data scrapped')
#
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="extract.py")
# geo_lat = []
# geo_long = []
#
# def geolocate(country):
#     try:
#         # Geolocate the center of the country
#         loc = geolocator.geocode(country)
#         # And return latitude and longitude
#         geo_lat.append(loc.latitude)
#         geo_long.append(loc.longitude)
#
#         return (loc.latitude, loc.longitude)
#     except:
#         # Return missing value
#         return '(0, 0)'
#
#
# #import scraped dataset
# data = pd.read_csv("covid19.csv")
# distributed_data = data
# data = distributed_data.dropna()
# #get the place cloumn
# geo_location = data.loc[: ,"place"]
#
# geo_location = geo_location.dropna()
# #convert to latitute and longtitute and save to list
# for location in geo_location:
#     if(location != ""):
#         # print(location)
#         geolocate(location)
#
# print('convaerted to latitute, longtitute')
#
# print(len(data),'df')
# print(data)
# print(len(geo_lat),'lati')
# print(len(geo_long),'longi')
#
# #adding to DF
# data['latitude'] = geo_lat
# data['longitude'] = geo_long
# print('added latitute, longtitute to DF')
#
# # print(data)
# import folium
# from folium.plugins import MarkerCluster
# #empty map
# world_map= folium.Map(tiles="cartodbpositron")
# marker_cluster = MarkerCluster().add_to(world_map)
#
# for i in range(len(data)):
#     if((data.iloc[i]['latitude']) != 0):
#         lat = data.iloc[i]['latitude']
#         long = data.iloc[i]['longitude']
#         radius=5
#         popup_text = """Country : {}"""
#         popup_text = popup_text.format(data.iloc[i]['place']
#                                    )
#         folium.CircleMarker(location = [lat, long], radius=radius, popup= popup_text, fill =True).add_to(marker_cluster)
# print('genertated map')
# world_map.save('world_map.html')

