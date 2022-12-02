import dash
import tweepy
from dash import dcc 
from dash import html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input,Output
from ConsumeAPI import api

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1('Extraccion de Tweets', style={'color':'hsl(216, 12%, 8%)'}),
        html.Img(src='/assets/twitterazul-removebg-preview.png')
    ], className='banner'),

    html.Div([
        html.Div([
            html.P("Buscar tweets",className='fix_label',style={'color':'black','margin-top':'2px'}),
            dcc.Input(
                id ='textInput',
                type = 'text', value='@',
                style={'align-content':'center','color':'black','align-items': 'center'},
                className='dcc_compon'
            ),
            
        ],className='create_container2 five columns',style={'margin-bottom':'20px'})
    ],className='flex-display'),
    
    html.Div([
        html.Div([
            html.H2('Numero de tweets',className='fix_label',style={'color':'black'}),
            dcc.Graph(id='bar_graph',figure={})
        ],className='create_container2 eight columns'),
        html.Div([
            html.H2('Plataformas',className='fix_label',style={'color':'black'}),
            dcc.Graph(id='pie_graph',figure={})
        ],className='create_container2 five columns'),
    ],className='row flex-display'),
    html.Div([
        html.Div([
            html.H2('Seguidores',className='fix_label',style={'color':'black'}),
            dcc.Graph(id='line_graph',figure={})
        ],className='create_container2 five columns'),
        html.Div([
            html.H2('Numero de Megusta',className='fix_label',style={'color':'black'}),
            dcc.Graph(id='disp_graph',figure={})
        ],className='create_container2 five columns'),
    ],className='row flex-display'),
    html.Div([
        html.Div([
            html.H2('Geolocalizacion',className='fix_label',style={'color':'black'}),
            dcc.Link(href='file:///C:/Cursos/ModelosSimulacion/SMRS/mapa.html')
        ],className='create_container2 five columns'),
    ],className='row flex-display'),

],id='mainContainer',style={'display':'flex','flex-direction':'column'})

@app.callback(
    Output('bar_graph', component_property='figure'),
    Output('pie_graph', component_property='figure'),
    Output('line_graph', component_property='figure'),
    Output('disp_graph', component_property='figure'),
    [Input('textInput',component_property='value')]
)

def update_graph(value):
    tweets=[]
    colum=['tweet','fecha','plataformas','favorites']

    #USUARIO# 
    cursor= tweepy.Cursor(api.user_timeline,screen_name=value, count =200, tweet_mode="extended").items(5000)
    for tweet in cursor:
        tweets.append([tweet.full_text,tweet.created_at.year,tweet.source,tweet.favorite_count])
    df=pd.DataFrame(tweets, columns=colum)
    Ctweets=df.groupby(['fecha'],as_index=False)[['tweet']].count()
    app=df.groupby(['plataformas'],as_index=False)[['tweet']].count()
    Cfavorites = df.groupby(['fecha'],as_index=False)[['favorites']].sum()
    #----------------------------------------------------------------
    #SEGUIDORES
    followers=[]
    columF=['seguidores','fecha']
    for follower in tweepy.Cursor(api.get_followers, screen_name=value,count=200).items(200):
        followers.append([follower.screen_name,follower.created_at.year])
    fll=pd.DataFrame(followers, columns=columF)
    Cfollowerd=fll.groupby(['fecha'],as_index=False)[['seguidores']].count()

    fig = px.bar(data_frame= Ctweets,
            x = 'fecha',
            y = 'tweet',opacity=0.9,
            template='plotly_dark',color='tweet'
        )
    
    fig2 = px.pie(
        data_frame= app,
        names='plataformas',
        values='tweet',template='plotly_dark'
        )
    
    fig3 = px.line(
        data_frame= Cfollowerd,
        x = 'fecha',
        y = 'seguidores',template='plotly_dark'
    )
    
    fig4 = px.scatter(
        data_frame= Cfavorites,
        x = 'fecha',
        y = 'favorites',template='plotly_dark'
    )
    return fig, fig2, fig3,fig4

if __name__ == ("__main__"):
    app.run_server(debug=True)