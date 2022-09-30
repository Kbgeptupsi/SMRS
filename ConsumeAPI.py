from os import access
from textwrap import indent
import tweepy
import json

#cadenas de autenticacion

consumer_key = "9ZX27Wd4njCVyDcr1gn0717K5"

consumer_secret ="1exIzHtQDkOs2qGTXI25syVwVchY1Y1HCiffjjD2JeEkC1PcT6"

access_token = "AAAAAAAAAAAAAAAAAAAAAFDtgwEAAAAArXjOOddf1kUWrwANWIUwl0Idkn0%3DnSupcOoDXrvlj"
access_token_secret = "tbIzM7QemfIKLQb00hBX0lPFcjHL0SwJ8fhV7"


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
wait_on_rate_limit_notify=True)


# obtenemos la informacion
data = api.me()
print json.dumps(data._json, indent=2)