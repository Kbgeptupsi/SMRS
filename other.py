import pandas as pd
import geopandas
import folium
import matplotlib.pyplot as plt
from folium import plugins
import tweepy
import pandas as pd
from geopy.geocoders import Nominatim

#cadenas de autenticacion
consumer_key ='jK2DckqU21HbasDgiIdfC4yaS'
consumer_secret ='TABB77LHsEB0pCKmRGTPW04wtuSLl0crzPoyUoPLBl52hjmwLh'
access_token = '1442525377352462339-D0EA5JlpIpDTdEmUNnic5X5VLlb3mK'
access_token_secret = 'm1jdObp4mQ7LRHX9cfjawH61K8rSpkowWGI158yB2GP5F'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=False)

tweets=[]
colum=['tweet','fecha','plataformas','favorites']

cursor= tweepy.Cursor(api.user_timeline,screen_name="@AdithBPerez", count =200, tweet_mode="extended").items(1)
map = folium.Map(location=[15, 30], tiles="Cartodb dark_matter", zoom_start=2)

for tweet in cursor:
    
    geo = Nominatim(user_agent='myapp')
    ubicacion=geo.geocode(tweet.user.location)

    map.add_child(
        folium.Marker(
            location=[ubicacion.latitude,ubicacion.longitude],
            popup=
                "Name: " + str(tweet.user.name) + "<br>",
            icon=folium.Icon(color="red"),
        )
    )

map.save("C:\\Cursos\\ModelosSimulacion\\SMRS\\mapa.html")