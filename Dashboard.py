import colorsys
from curses import COLOR_BLACK
import colorama
import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.dependencies import Input,Output

df = ''

app = dash.Dash(__name__)
df = pd.read_csv("df_bow_final.csv")[['N_like','N_comments','Latitude','Longitude','Fecha','Coordenadas','TopPosition']]
begin = datetime.strptime(df['Fecha'].min(),'%Y-%m-%d')
print(begin)
end=datetime.strptime(df['Fecha'].max(),'%Y-%m-%d')
print(end)
min_date='2022-06-20'
start_date='2022-08-01'
end_date='2022-10-01'
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
                type = 'text',
                style={'align-content':'center','color':'black'},
                className='dcc_compon'
            ),
            dcc.RadioItems(
                id ='dosis-radioitems',
                labelStyle= {'display':'inline-block'},
                options=[
                    {'label':'Primera dosis','value':'primera_dosis_cantidad'},
                ],value= 'primera_dosis_cantidad',
                style={'text-aling':'center','color':'black'},
                className='dcc_compon'
            )
        ],className='create_container2 five columns',style={'margin-bottom':'20px'})
    ],className='flex-display'),
    
    html.Div([
        html.Div([
            html.H2('Grafico de barras',className='fix_label',style={'color':'black'}),
            dcc.Graph(id='bar_graph',figure={})
        ],className='create_container2 eight columns'),
        html.Div([
            html.H2('Grafico de torta',className='fix_label',style={'color':'black'}),
            dcc.Graph(id='pie_graph',figure={})
        ],className='create_container2 five columns'),
    ],className='row flex-display'),
    html.Div([
        html.Div([
            html.H2('Grafico de linea',className='fix_label',style={'color':'black'}),
            dcc.Graph(id='line_graph',figure={})
        ],className='create_container2 five columns'),
    ],className='row flex-display'),
    html.Div([
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    calendar_orientation='horizontal',
                    day_size=39,
                    end_date_palceholder_text="return",
                    with_portal=False,
                    frint_day_of_week=0,
                    reopen_calendar_on_clear=True,
                    is_RTL=False,
                    clearable=True,
                    number_of_months_shown=1,
                    min_date_allowed=min_date,
                    max_date_allowed=end_date,
                    start_date=start_date,
                    end_date=end_date,
                    minimum_nights=2,
                    persistence=True,
                    persisted_props=['start_date'],
                    persisted_type='session',
                    updatemode='singledate'
                ),
                html.Div([
                    html.H2("twitter Tracker",className='fixlabel',style={'color':'black'}),
                    dcc.Graph(id='mymap')
                ],className='create_container2 five columns'),
             ],className='row flex-display'),
]
)
@app.callback(
    Output('bar_graph', component_property='figure'), 
    [Input('dosis-radioitems',component_property='value')]
)

def update_graph(value):
    if value == 'primera_dosis_cantidad':
        fig = px.bar(
            data_frame= df,
            x = 'jurisdiccion_nombre',
            y = 'primera_dosis_cantidad',
        )
    return fig

@app.callback(
    Output('pie_graph', component_property='figure'), 
    [Input('dosis-radioitems',component_property='value')]
)

def update_graph_pie(value):
    if value == 'primera_dosis_cantidad':
        fig2 = px.pie(
            data_frame= df,
            names='jurisdiccion_nombre',
            values='primera_dosis_cantidad'
            
        )
    return fig2

@app.callback(
    Output('line_graph', component_property='figure'), 
    [Input('dosis-radioitems',component_property='value')]
)

def update_graph_pie(value):
    if value == 'primera_dosis_cantidad':
        fig3 = px.line(
            data_frame= df,
            x = 'jurisdiccion_nombre',
            y = 'primera_dosis_cantidad',
        )
    return fig3
@app.callback(
     Output('mymap','figure')
    [Input('my-date-picker-range','start_date'),Input('my-date-picker-range','end_date')]
)
def update_map(begin,end):
    print(type(begin))
    print(end)
    df['fecha']=pd.to.datetime(df['fecha'])
    dff=df[df.fecha>=datetime.strptime(begin,'%Y-%m-%d')]
    print(df_map.head(10))
    df_map=dff.groupby(['TopPosition','Latitude','Longitude','Fecha']).sum()
    df_map['N_post']=dff.groupby(['TopPosition','Latitude','Longitude','Fecha']).count().Coordenadas
    df_map.reset_index(inplace=True)
    print(df_map.head(10))
    px.set_mapbox_access_token()
    fig=px.scatter_mapbox(df_map,lat='Latitude',lon='Longitude',hover_name='TopPosition',color='N_post',size='N_like',width=800,color_continuous_scale=px.colors.cyclical.IceFire,size_max=35,zoom=12)              
    fig.update_layaout(
        plot_bgcolor=COLOR_BLACK['background'],
        paper_bgcolor=colorama['background'],
        font_color=colorsys['text']
    )
    return fig

if __name__ == ("__main__"):
    app.run_server(port=8051)