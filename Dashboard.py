import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input,Output

df = ''

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1('SMRS',style={'font-family':'Verdana'}),
        html.B('  Sistema de monitoreo de redes sociales (twitter)',style={'color':'white','margin-top':'2px','font-family':'Arial'}),
        html.Img(src='/assets/twlog.png')
    ], className='banner'),

    html.Div([
        html.Div([
            # html.P("Buscar tweets",className='fix_label',style={'color':'black','margin-top':'4px','margin-bottom':'4px'}),
            dcc.Input(
                id ='textInput',
                type = 'text',
                style={'text-aling':'center','color':'black'},
                className='dcc_compon'
            ),
            html.Div(className='divseparador'),
            html.Button(' Buscar Tweets ',className='boton_buscar'),
        ],className='create_container2 five columns',style={'margin-bottom':'20px'})
    ],className='row flex-display'),
    
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

],id='mainContainer',style={'display':'flex','flex-direction':'column'})

@app.callback(
    Output('bar_graph', component_property='figure'), 
    [Input('textInput',component_property='value')]
)

def update_graph(value):
    if value == 'none':
        fig = px.bar(
            data_frame= df,
            x = 'x',
            y = 'y',
            title='Grafico de barras'
        )
    return fig

@app.callback(
    Output('pie_graph', component_property='figure'), 
    [Input('textInput',component_property='value')]
)

def update_graph_pie(value):
    if value == 'none':
        fig2 = px.pie(
            data_frame= df,
            title='Grafico de torta',
            names='n',
            values='v',
            
        )
    return fig2

@app.callback(
    Output('line_graph', component_property='figure'), 
    [Input('textInput',component_property='value')]
)

def update_graph_pie(value):
    if value == 'none':
        fig3 = px.line(
            data_frame= df,
            x='x',
            y='y',
            title='Grafico lineal'
        )
    return fig3

if __name__ == ("__main__"):
    app.run_server(port=8051)