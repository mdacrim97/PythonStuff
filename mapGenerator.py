import folium
import pandas
import csv
from geopy.geocoders import Nominatim

def rowCount(csvPath, Header):
    with open(csvPath, "r") as f:
        reader = csv.reader(f, delimiter = ",")
        data = list(reader)
        if Header == True:
            return len(data)-1
        return len(data)

####################################

yTownCoordinates = (41.102970, -80.647247)

#Generats map of youngstown
map = folium.Map(location=yTownCoordinates, zoom_start=12)

#open csv of yfd station locations.
locations = pandas.read_csv('yfdStations.csv')

#Plot station locations on map.
for each in locations[0:7].iterrows():
    folium.Marker([each[1]["latitude"], each[1]["longitude"]], popup=each[1]["Station No."]).add_to(map)

incidents = pandas.read_csv('yfd_sample_data.csv')

#Plot incident locations on map.
for each in incidents[0:rowCount('yfd_sample_data.csv', False)].iterrows():
    geolocator = Nominatim(user_agent="YDF_INCIDENTS")
    latLog = geolocator.geocode(each[1][3] + " Youngstown Ohio")
    if(latLog == None): continue
    lat =latLog.latitude
    log =latLog.longitude
    folium.Marker(location = [lat, log],
                  popup= "Code: " + str(each[1][4]) + "\n Date: " + each[1][1],
                  icon=folium.Icon(color='red')).add_to(map)

map.save('map.html')