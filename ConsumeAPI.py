import tweepy
import pandas as pd
#cadenas de autenticacion
consumer_key ='jK2DckqU21HbasDgiIdfC4yaS'
consumer_secret ='TABB77LHsEB0pCKmRGTPW04wtuSLl0crzPoyUoPLBl52hjmwLh'
access_token = '1442525377352462339-D0EA5JlpIpDTdEmUNnic5X5VLlb3mK'
access_token_secret = 'm1jdObp4mQ7LRHX9cfjawH61K8rSpkowWGI158yB2GP5F'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=False)
# tweets=[]
# colum=['tweet','fecha','plataformas']
# cursor= tweepy.Cursor(api.search_tweets,q='covid', tweet_mode="extended").items(10)
# for tweet in cursor:
#     tweets.append([tweet.full_text,tweet.created_at.year,tweet.source])
# df=pd.DataFrame(tweets, columns=colum)
# print(df)
