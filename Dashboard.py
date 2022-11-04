import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input,Output

df = pd.read_csv('Covid19VacunasAgrupadas.csv')

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
        html.Div([
            html.H2('Grafico de dispercion',className='fix_label',style={'color':'black'}),
            dcc.Graph(id='disp_graph',figure={})
        ],className='create_container2 five columns'),
    ],className='row flex-display'),

],id='mainContainer',style={'display':'flex','flex-direction':'column'})

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
    Output('disp_graph', component_property='figure'), 
    [Input('dosis-radioitems',component_property='value')]
)

def update_graph_pie(value):
    if value == 'primera_dosis_cantidad':
        fig4 = px.scatter(
            data_frame= df,
            x = 'jurisdiccion_nombre',
            y = 'primera_dosis_cantidad',
        )
    return fig4

if __name__ == ("__main__"):
    app.run_server(port=8051)