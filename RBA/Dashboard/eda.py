# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 18:57:28 2021

@author: Yara
"""
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from app import app
import pandas as pd
import  plotly.express as px

df_zscore1 = pd.read_csv('EDA_zscore1.csv')
df_zscore2 = pd.read_csv('EDA_zscore2.csv')
df_zscore3 = pd.read_csv('EDA_zscore3.csv')
df_zscore4 = pd.read_csv('EDA_zscore4.csv')
df_zscore5 = pd.read_csv('EDA_zscore5.csv')
df_zscore6 = pd.read_csv('EDA_zscore6.csv')
df_zscore7 = pd.read_csv('EDA_zscore7.csv')
df_zscore8 = pd.read_csv('EDA_zscore8.csv')
df_zscore9 = pd.read_csv('EDA_zscore9.csv')
df_zscore10 = pd.read_csv('EDA_zscore10.csv')

# df_zscore1_opp = pd.read_csv('EDA_zscore1_opp.csv')
# df_zscore2_opp = pd.read_csv('EDA_zscore2_opp.csv')
# df_zscore3_opp = pd.read_csv('EDA_zscore3_opp.csv')
# df_zscore4_opp = pd.read_csv('EDA_zscore4_opp.csv')
# df_zscore5_opp = pd.read_csv('EDA_zscore5_opp.csv')
# df_zscore6_opp = pd.read_csv('EDA_zscore6_opp.csv')
# df_zscore7_opp = pd.read_csv('EDA_zscore7_opp.csv')
# df_zscore8_opp = pd.read_csv('EDA_zscore8_opp.csv')
# df_zscore9_opp = pd.read_csv('EDA_zscore9_opp.csv')
# df_zscore10_opp = pd.read_csv('EDA_zscore10_opp.csv')

df_IQR1 = pd.read_csv('EDA_IQR1.csv')
df_IQR2 = pd.read_csv('EDA_IQR2.csv')
df_IQR3 = pd.read_csv('EDA_IQR3.csv')
df_IQR4 = pd.read_csv('EDA_IQR4.csv')
df_IQR5 = pd.read_csv('EDA_IQR5.csv')
df_IQR6 = pd.read_csv('EDA_IQR6.csv')
df_IQR7 = pd.read_csv('EDA_IQR7.csv')
df_IQR8 = pd.read_csv('EDA_IQR8.csv')
df_IQR9 = pd.read_csv('EDA_IQR9.csv')
df_IQR10 = pd.read_csv('EDA_IQR10.csv')

# df_IQR1_opp = pd.read_csv('EDA_IQR1_opp.csv')
# df_IQR2_opp = pd.read_csv('EDA_IQR2_opp.csv')
# df_IQR3_opp = pd.read_csv('EDA_IQR3_opp.csv')
# df_IQR4_opp = pd.read_csv('EDA_IQR4_opp.csv')
# df_IQR5_opp = pd.read_csv('EDA_IQR5_opp.csv')
# df_IQR6_opp = pd.read_csv('EDA_IQR6_opp.csv')
# df_IQR7_opp = pd.read_csv('EDA_IQR7_opp.csv')
# df_IQR8_opp = pd.read_csv('EDA_IQR8_opp.csv')
# df_IQR9_opp = pd.read_csv('EDA_IQR9_opp.csv')
# df_IQR10_opp = pd.read_csv('EDA_IQR10_opp.csv')


df_EDA1_final = pd.read_csv('res11.csv')
df_EDA2_final = pd.read_csv('res21.csv')
df_EDA3_final = pd.read_csv('res31.csv')
df_EDA4_final = pd.read_csv('res41.csv')
df_EDA5_final = pd.read_csv('res51.csv')
df_EDA6_final = pd.read_csv('res61.csv')
df_EDA7_final = pd.read_csv('res71.csv')
df_EDA8_final = pd.read_csv('res81.csv')
df_EDA9_final = pd.read_csv('res91.csv')
df_EDA10_final = pd.read_csv('res101.csv')



layout= html.Div(children=[
    html.Br(),
    html.Br(),
    html.Br(),
    dcc.Tabs(id='tabs', value='tab-1', children=[
         dcc.Tab(label='Z-score Method', value='tab-1', id='tab1', children =[
             html.Div(children = [
            html.Br(),
            html.H6('-------'),
            
            dcc.Dropdown(
                    id="dropdown-1",
                    options=[{"label": 'House 1', "value": 'z1'},
                             {"label": 'House 2', "value": 'z2'},
                             {"label": 'House 3', "value": 'z3'},
                             {"label": 'House 4', "value": 'z4'},
                             {"label": 'House 5', "value": 'z5'},
                             {"label": 'House 6', "value": 'z6'},
                             {"label": 'House 7', "value": 'z7'},
                             {"label": 'House 8', "value": 'z8'},
                             {"label": 'House 9', "value": 'z9'},
                             {"label": 'House 10', "value": 'z10'}
                             
                    ],
                    value="z1",
                ),
            
             html.Div(children=[
          html.Div(
        dcc.Graph(id='EDA-data1'), style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}
              ),
          html.Div(
          dcc.Graph(id='boxplt-EDA1') , style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}
              ),
          ]),
            
            ])
             ]),
         
         dcc.Tab(label='IQR Method', value='tab-2', id='tab2', children = [
              html.Div(children = [
            html.Br(),
            html.H6('-------'),
            
            dcc.Dropdown(
                    id="dropdown-2",
                    options=[{"label": 'House 1', "value": 'i1'},
                             {"label": 'House 2', "value": 'i2'},
                             {"label": 'House 3', "value": 'i3'},
                             {"label": 'House 4', "value": 'i4'},
                             {"label": 'House 5', "value": 'i5'},
                             {"label": 'House 6', "value": 'i6'},
                             {"label": 'House 7', "value": 'i7'},
                             {"label": 'House 8', "value": 'i8'},
                             {"label": 'House 9', "value": 'i9'},
                             {"label": 'House 10', "value": 'i10'}
                             
                    ],
                    value="i1",
                ),
            
             html.Div(children=[
          html.Div(
        dcc.Graph(id='EDA-data2'), style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}
              ),
          html.Div(
          dcc.Graph(id='boxplt-EDA2') , style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}
              ),
          ]),
            
            ])
              ]),
         
         dcc.Tab(label='Final Outliers Removal', value='tab-3', id='tab3', children = [
              html.Div(children = [
            html.Br(),
            html.H6('-------'),
            
            dcc.Dropdown(
                    id="dropdown-3",
                    options=[{"label": 'House 1', "value": 'f1'},
                             {"label": 'House 2', "value": 'f2'},
                             {"label": 'House 3', "value": 'f3'},
                             {"label": 'House 4', "value": 'f4'},
                             {"label": 'House 5', "value": 'f5'},
                             {"label": 'House 6', "value": 'f6'},
                             {"label": 'House 7', "value": 'f7'},
                             {"label": 'House 8', "value": 'f8'},
                             {"label": 'House 9', "value": 'f9'},
                             {"label": 'House 10', "value": 'f10'}
                             
                    ],
                    value="f1",
                ),
            
             html.Div(children=[
          html.Div(
        dcc.Graph(id='EDA-data3'), style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}
              ),
          html.Div(
          dcc.Graph(id='boxplt-EDA3') , style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}
              ),
          ]),
            
            ])
              ]),
            
    ]), 
    
])

@app.callback(
    Output('EDA-data1', 'figure'),
    Output('boxplt-EDA1', 'figure'),
    [Input('dropdown-1', 'value')])
def prepare_eda_graphs1(value):
    if (value == 'z1'): 
        return {
        'data': [
            {'x': df_zscore1.Date, 'y': df_zscore1['Energy_res1'], 'type': 'scatter'},      
        ],
        'layout': {
            'title': 'After removal by Z-score method '  
        } }, px.box(df_zscore1, x=df_zscore1['Energy_res1'])
    elif (value == 'z2'):
        return {
        'data': [
            {'x': df_zscore2.Date, 'y': df_zscore2['Energy_res2'], 'type': 'scatter'},      
        ],
        'layout': {
            'title': 'After removal by Z-score method '  
        } }, px.box(df_zscore2, x=df_zscore2['Energy_res2'])
    elif (value == 'z3'):
        return {
        'data': [
            {'x': df_zscore3.Date, 'y': df_zscore3['Energy_res3'], 'type': 'scatter'},      
        ],
        'layout': {
            'title': 'After removal by Z-score method '  
        } }, px.box(df_zscore3, x=df_zscore3['Energy_res3'])
    
 
         
@app.callback(
    Output('EDA-data2', 'figure'),
    Output('boxplt-EDA2', 'figure'),
    [Input('dropdown-2', 'value')])
def prepare_eda_graphs2(value):
    if (value == 'i4'): 
        return {
        'data': [
            {'x': df_IQR4.Date, 'y': df_IQR4['Energy_res4'], 'type': 'scatter'},      
        ],
        'layout': {
            'title': 'After removal by Z-score method '  
        } }, px.box(df_IQR4, x=df_IQR4['Energy_res4'])
    elif (value == 'z5'):
        return {
        'data': [
            {'x': df_IQR5.Date, 'y': df_IQR5['Energy_res5'], 'type': 'scatter'},      
        ],
        'layout': {
            'title': 'After removal by Z-score method '  
        } }, px.box(df_IQR5, x=df_IQR5['Energy_res5'])
    elif (value == 'z6'):
        return {
        'data': [
            {'x': df_IQR6.Date, 'y': df_IQR6['Energy_res6'], 'type': 'scatter'},      
        ],
        'layout': {
            'title': 'After removal by Z-score method '  
        } }, px.box(df_IQR6, x=df_IQR6['Energy_res6'])
    
    
@app.callback(
    Output('EDA-data3', 'figure'),
    Output('boxplt-EDA3', 'figure'),
    [Input('dropdown-3', 'value')])
def prepare_eda_graphs3(value):
    if (value == 'f7'): 
        return {
        'data': [
            {'x': df_EDA7_final.Date, 'y': df_EDA7_final['Energy_res7'], 'type': 'scatter'},      
        ],
        'layout': {
            'title': 'After removal by Z-score method '  
        } }, px.box(df_EDA7_final, x=df_EDA7_final['Energy_res7'])
    elif (value == 'f8'):
        return {
        'data': [
            {'x': df_EDA8_final.Date, 'y': df_EDA8_final['Energy_res8'], 'type': 'scatter'},      
        ],
        'layout': {
            'title': 'After removal by Z-score method '  
        } }, px.box(df_EDA8_final, x=df_EDA8_final['Energy_res8'])
    elif (value == 'f9'):
        return {
        'data': [
            {'x': df_EDA9_final.Date, 'y': df_EDA9_final['Energy_res9'], 'type': 'scatter'},      
        ],
        'layout': {
            'title': 'After removal by Z-score method '  
        } }, px.box(df_EDA9_final, x=df_EDA9_final['Energy_res9'])
