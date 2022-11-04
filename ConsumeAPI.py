import tweepy
import json

# 4 cadenas para la autenticacion
consumer_key = "9ZX27Wd4njCVyDcr1gn0717K5"
consumer_secret = "1exIzHtQDkOs2qGTXI25syVwVchY1Y1HCiffjjD2JeEkC1PcT6"
access_token = "AAAAAAAAAAAAAAAAAAAAAFDtgwEAAAAArXjOOddf1kUWrwANWIUwl0Idkn0%3DnSupcOoDXrvlj"
access_token_secret = "tbIzM7QemfIKLQb00hBX0lPFcjHL0SwJ8fhV7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret,access_token,access_token_secret)
auth.set_access_token(access_token, access_token_secret)
# con este objeto realizaremos todas las llamadas al API
api = tweepy.API(auth,wait_on_rate_limit=True)

#Obtener informacion de otros usarios
user = api.get_user("maradona")
#
print (json.dumpsuser._json)

#Obtener followers
data = api.get_followers(screen_name="nike")

for user in data:
    print (json.dumps(user._json, indent=4))
    #print len(data)
 # Explicar cursor
for user in tweepy.Cursor(api.followers, screen_name="obama").items():
    print (json.dumps(user._json, indent=4))

#Obtener followees
for user in tweepy.Cursor(api.friends, screen_name="obama").items(2):
    print (json.dumps(user._json, indent=4))

#Obtener un timeline
for tweet in tweepy.Cursor(api.user_timeline, screen_name="obma", tweet_mode="extended").items(10):
    print (json.dumps(tweet._json,  indent=4))

#Buscar Tweets
for tweet in tweepy.Cursor(api.search, q="messi bdo", tweet_mode="extended").items(5):
    print (json.dumps(tweet._json, indent=4))
