import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html, dcc, dash_table, callback, Input, Output
import datetime
import json
import numpy as np


# ________________________________________ definition des variables _____________________________________________ #


data = pd.read_csv('test_new.csv', sep='\t')
old = pd.read_csv('test.csv', sep='\t')
monthly = pd.read_csv('test_all.csv', sep='\t')

list_countries = ['Angola', 'Comoros', 'Kenya', 'Madagascar', 'Mauritius', 'Mozambique',
                'Namibia', 'Seychelles', 'Tanzania']

outputs = {
    'Output1-1-6': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                    'tickval': [0, 25, 50, 75, 100],
                    'title': 'Number of effective reviews of existing national legislation related to port security '
                             'and maritime safety management completed.'},
    'Output1-1-7': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                    'tickval': [0, 25, 50, 75, 100],
                    'title': 'Number of proposals for adaption to national legislation.'},
    'Output1-1-8': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                    'tickval': [0, 25, 50, 75, 100],
                    'title': 'Number of personnel from judicial stakeholders trained on ensuring a legal finish to '
                             'prosecutions of port related crimes.'},
    'Output1-1-9': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                    'tickval': [0, 25, 50, 75, 100],
                    'title': 'An initiation or increase in the number of prosecutions related to port safety and '
                             'security measures.'},
    'Output1-1-10': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Number of obstacles found that hamper the transposition of international main agreements'
                              ' and legislations into national legislation.'},
    'Output1-2-22': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Number of participants in training on the related subjects.'},
    'Output1-2-23': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Number of cases prosecuted in accordance with maritime legislation.'},
    'Output2-1-24': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Number of ports having implemented the ISPS code and related regulatory '
                              'compliance frameworks.'},
    'Output2-2-30': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Number of  port or port facility security assessments completed.'},
    'Output2-2-31': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Number of Port Security Plans developed and implemented.'},
    'Output2-2-32': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Number of port staff trained in security, risk and incident management.'},
    'Output2-2-33': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Status of contingency plans and evacuation plans for different emergency '
                              'situations/threats.'},
    'Output2-2-34': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Status of risk assessment for the ports facilities.'},
    'Output2-2-35': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Number of emergency exercises conducted with the support of this Action '
                              '(disaggregated per country).'},
    'Output2-2-36': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Number of port security drills and exercises developed and delivered.'},
    'Output2-2-40': {'range': [0, 100], 'ticktext': ['0%', '25%', '50%', '75%', '100%'],
                     'tickval': [0, 25, 50, 75, 100],
                     'title': 'Number of Port Control Unit established in EA-SA-IO Region'},
    }

objective_dd = []
for output in outputs:
    objective_dd.append({'label': outputs[output]['title'], 'value': output})

objective_dd.insert(0, {'label': 'Overall project achievement', 'value': 'all'})

#print(data)

start = datetime.datetime(2022, 1, 1)
end = datetime.datetime(2023, 12, 31)
today = datetime.datetime(2022, 5, 31) # datetime.datetime.today()
all_time = end-start
past_time = today-start
progression = past_time/all_time*100

nb_clicks = 0


# ______________________________________________________ Layout  _____________________________________________________ #

layout = html.Div([html.H5('Select an indicator'),
                   html.Div(dcc.Dropdown(id="select_indicator", options=objective_dd, value='all', multi=False),
                            style={'padding':20}),
                   html.Br(),
                    html.H5('Select countries'),

                   html.Div(dcc.Dropdown(id="select_countries", options=list_countries, value='All',multi=True),
                            style={'padding':20}),
                    html.Br(),
                    html.H2('Overall progression',style={'text-align':'center'}),
                    html.Br(),
                   html.Div(
                       [html.Div(style={'width': '5%'}),
                        html.Div(dcc.Graph(id='indicator_progression'), style={'width': '50%'}),
                        html.Div(style={'width': '5%'}),
                        html.Div(children = [html.Br(),dash_table.DataTable(id='indicator_table')],
                                style={'width': '35%','border-top':50}),
                        html.Div(style={'width': '5%'}),
                        ],
                       style={'display':'flex'}

                   ),
                    html.Br(),
                    html.H2('Monthly evolution since the beginning of the project',style={'text-align':'center'}),
                    html.Br(),
                   html.Div(
                       [html.Div(style={'width': '5%'}),
                        html.Div(children = dcc.Graph(id='indicator_evolution'), style={'width': '50%'}),
                        html.Div(style={'width': '5%'}),
                        html.Div(children=[html.Br(),dash_table.DataTable(id='indicator_table2')],
                                 style={'width': '35%','border-top':50}),
                        html.Div(style={'width': '5%'}),
                        ],
                       style={'display': 'flex'}

                   )
                   ],  # Dropdown obj to remove (select by click)
                style={'padding': 10})



@callback([Output(component_id='indicator_progression', component_property='figure'),
                Output(component_id='indicator_table', component_property='data'),
           Output(component_id='indicator_evolution', component_property='figure'),
           Output(component_id='indicator_table2', component_property='data')],
                [Input(component_id="select_indicator", component_property='value'),
                 Input(component_id="select_countries", component_property='value')])
def update_graphs(indicateur, liste_pays):
    # print(liste_pays)
    df=pd.DataFrame(columns=['Country','Old progression','New progression','Target'])
    if liste_pays=='All':
        df['Country']=data.drop(9,axis=0)['Country']
        df['Old progression'] = old.drop(9, axis=0)[indicateur]
        df['New progression'] = data.drop(9, axis=0)[indicateur]
        df['Target']=np.ones(len(df))*100
    else:
        df['Country'] = data[data['Country'].isin(liste_pays)]['Country']
        df['Old progression'] = old[old['Country'].isin(liste_pays)][indicateur]
        df['New progression'] = data[data['Country'].isin(liste_pays)][indicateur]
        df['Target'] = np.ones(len(df)) * 100
    if indicateur=='all':
        df['Old progression'] = df['Old progression']/16
        df['New progression'] = df['New progression']/16

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=df['Country'],
        x=df['Old progression'],
        name='Last progression',
        orientation='h',
        marker=dict(
            color='rgba(246, 78, 139, 0.6)',
            line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
    ))
    fig.add_trace(go.Bar(
        y=df['Country'],
        x=df['New progression']-df['Old progression'],
        name='Recent progression',
        orientation='h',
        marker=dict(
            color='rgba(58, 71, 80, 0.6)',
            line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
        )
    ))
    fig.add_vline(x=progression, line_width=3, line_dash="dash", line_color="green",
                annotation_text = "time passed",
                      annotation_position = "top",
                                            annotation_font_size = 20,
                                                                   annotation_font_color = "green"
    )

    fig.update_layout(barmode='stack',margin={'l':20,'r':20,'b': 20,'t': 30})
    #fig.update_traces(margin={'l':20,'r':20,'b': 20,'t': 20})

    dico_data=df.to_dict('records')

    df=pd.DataFrame()

    if liste_pays != 'All':
        df_all = monthly[monthly['Country'].isin(liste_pays)].copy()
    else:
        df_all = monthly[monthly['Country'] != 'All'].copy()

    df['Country']=df_all[df_all['month']=='January']['Country']

    # print(df_all)
    a=np.zeros(len(df))

    for month in monthly['month'].unique():
        # print(month)
        b=df_all[df_all['month'] == month][indicateur].values
        # print(b)
        if indicateur == 'all':
            b = b / 16
        df[month]=a+b
        a=df[month]

    fig2 = go.Figure()
    for pays in df['Country'].unique():
        print(df[df['Country']==pays][monthly['month'].unique()].iloc[0])
        fig2.add_trace(go.Scatter(x=monthly['month'].unique(),
                                 y=df[df['Country']==pays][monthly['month'].unique()].iloc[0],
                                 mode='lines',
                                 name=pays))
    fig2.update_layout(margin={'l': 20, 'r': 20, 'b': 20, 't': 30})
    dico_data2 = df.to_dict('records')




    return fig, dico_data, fig2, dico_data2


