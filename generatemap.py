import pandas as pd
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="generatemap.py")
geo_lat = []
geo_long = []

def geolocate(country):
    try:
        # Geolocate the center of the country
        loc = geolocator.geocode(country)
        # And return latitude and longitude
        geo_lat.append(loc.latitude)
        geo_long.append(loc.longitude)

        return (loc.latitude, loc.longitude)
    except:
        # Return missing value
        print('error ',country)
        return ''


#import scraped dataset
data = pd.read_csv("covid19.csv")
distributed_data = data
data = distributed_data.dropna()
#get the place cloumn
geo_location = data.loc[: ,"place"]

geo_location = geo_location.dropna()
#convert to latitute and longtitute and save to list
for location in geo_location:
    if(location != ""):
        # print(location)
        geolocate(location)

print('convaerted to latitute, longtitute')

print(len(data),'df')
print(data)
print(len(geo_lat),'lati')
print(len(geo_long),'longi')

#adding to DF
data['latitude'] = geo_lat
data['longitude'] = geo_long
print('added latitute, longtitute to DF')

# print(data)
import folium
from folium.plugins import MarkerCluster
#empty map
world_map= folium.Map(tiles="cartodbpositron")
marker_cluster = MarkerCluster().add_to(world_map)

for i in range(len(data)):
    if((data.iloc[i]['latitude']) != 0):
        lat = data.iloc[i]['latitude']
        long = data.iloc[i]['longitude']
        radius=5
        popup_text = """Country : {}"""
        popup_text = popup_text.format(data.iloc[i]['place']
                                   )
        folium.CircleMarker(location = [lat, long], radius=radius, popup= popup_text, fill =True).add_to(marker_cluster)
print('genertated map')
world_map.save('world_map.html')