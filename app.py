import dash
import dash_bootstrap_components as dbc
import twitter

api = twitter.Api(consumer_key='aA7ezlQBvomntgkIxOePqjc6J',
                      consumer_secret='RlWPHHkGOgWxKaNaYnxbty24Hbvs1kNE7UcTurOaYlxeXjDUPp',
                      access_token_key='964286914638569472-tIAMlN9HUaIZFAasOtpQE9nCXg9Zf51',
                      access_token_secret='vbm6vKqG6AYXFBU65G85bATi9skJXmNed8LMsJ2NmH1Py')
# ensure you connected correctly
# print(api.VerifyCredentials())
# exit()

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LUX],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )