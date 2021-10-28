import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import numpy as np
import os
def generate_table(dataframe):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(len(dataframe))
        ])
    ])

def graph_residuales(residuales, campo_grupos='grupo'):
    colores = ['#FCE688','#0000FF','#FF9933','#FF00FF','#66FFFF','#00B050','#7F7F7F','#00B0F0','#000000','#FF0000','#99FF33','#CC99FF','#D9D9D9']
    criterios = list(residuales.columns)[1:-1]
    fig = px.bar(residuales, x=campo_grupos, y=criterios, barmode="group",color_discrete_sequence=colores)
    return fig

app = dash.Dash(__name__)
server = app.server
dirname = os.path.dirname(__file__)

#residuales_e07 = pd.read_excel(os.path.join(dirname,"bd_residuales_esc/e07/bd_residuales_grupos_v1.xlsx"),engine='openpyxl')
residuales_e08 = pd.read_excel(os.path.join(dirname,"bd_residuales_esc/e08/bd_residuales_grupos_v1.xlsx"),engine='openpyxl')
residuales_e09 = pd.read_excel(os.path.join(dirname,"bd_residuales_esc/e09/bd_residuales_grupos_v1.xlsx"),engine='openpyxl')
residuales_e10 = pd.read_excel(os.path.join(dirname,"bd_residuales_esc/e10/bd_residuales_grupos_v1.xlsx"),engine='openpyxl')
#data = pd.read_excel("C:/Dropbox (LANCIS)/CARPETAS_TRABAJO/apc_temeraria/politetico_divisivo/e08/bd_grupos_v1_e08_22_oct2021.xlsx",engine='openpyxl',sheet_name='sintesis_grupos')

dicc_res_esc = {
    'e08v1':{'grafica':graph_residuales(residuales_e08),'desc':"Incluye 13 sectores (sin pesca ni acuacultura), incluye ANP federales y estatales. 12 sectores con CLP, el mapa de aptitud de conservación sin incluir ANP como aprovechamiento actual. 1 sector con OWA mínimo: Bovino"},
    'e09v1':{'grafica':graph_residuales(residuales_e09),'desc':"Incluye 13 sectores (sin pesca ni acuacultura), incluye ANP federales y estatales. 11 sectores con CLP, el mapa de aptitud de conservación sin incluir ANP como aprovechamiento actual. 2 sectores con OWA mínimo: Bovino, Porcino avícola"},
    'e10v1':{'grafica':graph_residuales(residuales_e10),'desc':"Incluye 13 sectores (sin pesca ni acuacultura), incluye ANP federales y estatales. 12 sectores con CLP, el mapa de aptitud de conservación sin incluir ANP como aprovechamiento actual. 1 sector con OWA mínimo: Forestal"},
                }

data =[]
for i,v in dicc_res_esc.items():

    data.append(html.H2(children=i,style={'textAlign': 'center'}))
    data.append(dcc.Markdown(style={'textAlign': 'center'},children=v["desc"]))
    data.append(dcc.Graph(id=i,figure=v["grafica"]))

app.layout = html.Div(children=data)


if __name__ == '__main__':
    app.run_server(debug=True)