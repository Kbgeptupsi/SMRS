import tweepy
import json

#cadenas de autenticacion

API_KEY="fn4GQZUx1E46gBcSFbX9rXT9y"
API_SECRET_KEY="LG0Bjwteu9gkeV7pj0zWoPaeF2jtjSSUbuv8XgMeChu2RobVG9"
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAANcPhAEAAAAACH596ukEf9hBWi7rHRbPWDl3LIc%3D7tjKsFca1EXXVyrH72BHfOdCnmJkEL0GY7kiJmLXh4oNhdHORc"
ACCESS_TOKEN="1442525377352462339-rBKONpUOsw9zyUzPfYaXapEZumLWx1"
ACCESS_TOKEN_SECRET="KA1uA9sr82hbd5iR02TgtK0wFq0Qizh3urahMdou7ZpYK"

auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


# obtenemos la informacion
data = api.home_timeline
print (data.__format__)