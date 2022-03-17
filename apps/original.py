import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
import datetime
import json
from dash.dependencies import Output, Input

# --------------------------------- Fonction affichage indicateurs -------------------------------------------------- #


def retard(temps, k):
    if k > 1.1 * temps:
        return 'green'
    elif k > temps:
        return 'lightgreen'
    elif k > 0.95 * temps:
        return 'yellow'
    elif k > 0.9 * temps:
        return 'yellow'
    else:
        return 'red'


def indicateur(domaine, ticktext, tickval, title, progression_temps, progression_objectif, couleur):
    indic = go.Figure(go.Indicator(
        mode="gauge",
        gauge={'shape': "bullet",
               'axis': {'range': domaine, 'tickmode': 'array', 'ticktext': ticktext,
                        'tickvals': tickval},
               'threshold': {
                   'line': {'color': "black", 'width': 2},
                   'thickness': 1,
                   'value': progression_temps},
               'bar': {'color': couleur, 'thickness': 0.7}
               },
        value=progression_objectif,
        domain={'x': [0, 1], 'y': [0, 1]},
    ))
    indic.update_layout(title=title, title_x=0.5,
                       title_xanchor='center',
                       height=100, margin_b=40, margin_t=40, margin_r=40, margin_l=40)

    return indic


# ________________________________________ definition des variables _____________________________________________ #


app = dash.Dash(__name__)
server = app.server

data = pd.read_csv('test.csv', sep='\t')

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

print(data)

start = datetime.datetime(2022, 1, 1)
end = datetime.datetime(2023, 12, 31)
today = datetime.datetime.today()
all_time = end-start
past_time = today-start
progression = past_time/all_time*100

nb_clicks = 0

fig = indicateur([0, all_time.total_seconds()], [2022, 2023, 2024],  # Indicateur temps
                 [0, all_time.total_seconds() / 2, all_time.total_seconds()],
                 f'Time passed since the project started: {round(progression)}%',
                 past_time.total_seconds(), past_time.total_seconds(), 'blue')
fig_hidden = indicateur([0, all_time.total_seconds()], [2022, 2023, 2024],
                      [0, all_time.total_seconds() / 2, all_time.total_seconds()],
                      f'Time passed since the project started: <b>{round(progression)}</b>%',
                      past_time.total_seconds(), past_time.total_seconds(), 'blue')

# ______________________________________________________ Layout  _____________________________________________________ #

app.layout = html.Div([html.Div(html.H1("Port Security and Safety of Navigation in Eastern andSouthern Africa and the "
                                        "Indian Ocean - EU"),
                                style={"text-align": "center", "background-color": "lightblue"}),    # Title
                    html.Div(dcc.Graph(figure=fig), style={"border-style": "solid"}),
                       html.Div(dcc.Dropdown(id="select_obj", options=objective_dd, value='all', multi=False),
                                ),  # Dropdown obj to remove (select by click)
                       html.Div(dcc.Graph(id='objective_target'), style={"border-style": "solid"}),
                       # Proj/Obj completion
                       html.Br(),
                       html.Div([
                           html.Div([html.H3(id='outcome1', children='Reinforcement of the capacities of Maritime '
                                                                     'Affairs Authorities and governmental agencies.'),
                                     html.Div(id='O6', children=dcc.Graph(id="Output1-1-6")),
                                     html.Div(id='O7', children=dcc.Graph(id="Output1-1-7")),
                                     html.Div(id='O8', children=dcc.Graph(id="Output1-1-8")),
                                     html.Div(id='O9', children=dcc.Graph(id="Output1-1-9")),
                                     html.H3(id='outcome2', children='Identification of obstacles hampering the '
                                                                     'transposition of international main agreements '
                                                                     'and legislations into national legislation.'),
                                     html.Div(id='O10', children=dcc.Graph(id="Output1-1-10")),
                                     ],
                                    style={"display": "flex", "flex-direction": "column", "width": "16%"}),
                           html.Div([html.H2(id='text_map', style={"text-align": "center"}),
                                     html.Div(id='carte', children=dcc.Graph(id='carte2'), n_clicks=0),
                                     html.Div([
                                         html.Div([
                                             html.H3(id='outcome3', children='Improved capacity building on Port State '
                                                                             'Control measures in relation to '
                                                                             'criminality aspects such as standard '
                                                                             'operating procedures, communications '
                                                                             'procedures, personnel security and so on'
                                                                             '.'),
                                             html.Div(id='O22', children=dcc.Graph(id="Output1-2-22")),
                                             html.Div(id='O23', children=dcc.Graph(id="Output1-2-23"))
                                                ], style={"display": "flex", "flex-direction": "column",
                                                          "justify-content": "flex-start", "width": '25%'}),
                                         html.Div(style={"display": "flex", "flex-direction": "column",
                                                         "justify-content": "flex-start", "width": '20%'}),
                                         html.Div([
                                             html.H3(id='outcome4', children='Implementation of ISPS Code and related '
                                                                             'compliance framework adopted by ports of '
                                                                             'the EA-SA-IO region. '),
                                             html.Div(id='O24', children=dcc.Graph(id="Output2-1-24")),
                                             ], style={"display": "flex", "flex-direction": "column",
                                                      "justify-content": "flex-start", "width": '25%'}),
                                         html.Div(style={"display": "flex", "flex-direction": "column",
                                                         "justify-content": "flex-start", "width": '5%'}),
                                         html.Div([
                                             html.H3(id='outcome6', children='Implementation of a cargo targeting '
                                                                             'system for risky consignments to enhance '
                                                                             'customs clearance of goods as prescribed '
                                                                             'by international best practices. '),
                                             html.Div(id='O40', children=dcc.Graph(id="Output2-2-40")),
                                             ], style={"display": "flex", "flex-direction": "column",
                                                      "justify-content": "flex-start", "width": '25%'})
                                            ], style={"display": "flex"})
                                     ], style={"display": "flex", "flex-direction": "column",
                                              "justify-content": "flex-start", "width": '66%'}),
                           html.Div([html.H3(id='outcome5', children='Develop and support the implementation of Port '
                                                                     'security management in the EA-SA-IO Region.',
                                             ),
                                    html.Div(id='O30', children=dcc.Graph(id="Output2-2-30")),
                                    html.Div(id='O31', children=dcc.Graph(id="Output2-2-31")),
                                    html.Div(id='O32', children=dcc.Graph(id="Output2-2-32")),
                                    html.Div(id='O33', children=dcc.Graph(id="Output2-2-33")),
                                    html.Div(id='O34', children=dcc.Graph(id="Output2-2-34")),
                                    html.Div(id='O35', children=dcc.Graph(id="Output2-2-35")),
                                    html.Div(id='O36', children=dcc.Graph(id="Output2-2-36")),
                                     ],
                                    style={"display": "flex", "flex-direction": "column", "width": "16%"}),
                       ], style={"display": "flex"})
                       ])

divs = ['O6', 'O7', 'O8', 'O9', 'O10', 'O22', 'O23', 'O24', 'O30', 'O31', 'O32', 'O33', 'O34', 'O35', 'O36', 'O40']
names = data.columns.tolist()[1:-1]


@app.callback([Output(component_id='objective_target', component_property='figure'),
               Output(component_id='carte2', component_property='figure'),
               Output(component_id='carte', component_property='n_clicks'),
               Output(component_id='text_map', component_property='children')] +
            [Output(component_id=i, component_property='figure') for i in names] +
            [Output(divs[i], 'style') for i in range(16)]+[Output(divs[i], 'title') for i in range(16)] +
            [Output(component_id='outcome'+str(i), component_property='style') for i in range(1, 7)],
            [Input(component_id="select_obj", component_property='value'),
             Input('carte', 'n_clicks'), Input('carte2', 'clickData')])
def update_graphs(obj, clicks, what):
    print('What ', what)
    print('clicks ', clicks)
    print('obj', obj)
    # Liste indicateurs
    fig6 = fig7 = fig8 = fig9 = fig10 = fig22 = fig23 = fig24 = fig30 = fig31 = fig32 = fig33 = fig34 = fig35 = fig36 =\
        fig40 = go.Figure()
    outputs_fig = [fig6, fig7, fig8, fig9, fig10, fig22, fig23, fig24, fig30, fig31, fig32, fig33, fig34, fig35, fig36,
               fig40]
    styles = [{} for _ in range(16)]
    outcomes_styles = [{} for _ in range(6)]
    position_pays = ['', 'Angola', 'Namibia', '', '', '', '', 'Mozambique', 'Kenya', 'Seychelles', 'Tanzania',
                     'Madagascar', 'Mauritius', '', '', 'Comoros']

    if clicks != 0:
        what = None

    if what is not None:

        country = what['points'][0]['location']
        country_coord = data[data['Country'] == country].copy()
        countries = data[data['Country'] == country].copy()
        overall_progression = country_coord['all'].values[0] / 18
        fig2 = indicateur([0, 100], ['0', '25%', '50%', '75%', '100%'], [0, 25, 50, 75, 00],
                          f'Project overall completion in {country}', progression,
                        overall_progression, retard(progression, overall_progression))
        print(country)
        print(country_coord)

        if obj == 'all':
            titles = [outputs[i]['title'] for i in outputs]
            for i in range(16):
                indic = data.columns.tolist()[1:-1][i]
                progress = country_coord[indic].values[0]

                outputs_fig[i] = indicateur(outputs[indic]['range'], outputs[indic]['ticktext'],
                                            outputs[indic]['tickval'], indic, progression, progress,
                                            retard(progression, progress))
            text_map = f'Different indicators completion in {country} since the beginning of the project'

        else:
            titles = position_pays
            progress = country_coord[obj].values[0]
            outcomes_styles = [{"display": "none"} for _ in range(6)]
            for i in range(16):
                if position_pays[i] == country:
                    outputs_fig[i] = indicateur(outputs[obj]['range'], outputs[obj]['ticktext'],
                                                outputs[obj]['tickval'], obj, progression, progress,
                                                retard(progression, progress))

                else:
                    outputs_fig[i] = indicateur(outputs[obj]['range'], outputs[obj]['ticktext'],
                                                outputs[obj]['tickval'], obj,
                                                progression, progress, retard(progression, progress))
                    styles[i] = {"visibility": "hidden"}
            text_map = f'Completion of indicator: {outputs[obj]["title"]}'

    # indicateur(range, ticktext, tickval, title, progression_temps, progression_objectif, couleur)

    else:
        country = 'All'
        countries = data.drop([9], axis=0).copy()
        country_coord = data[data['Country'] == country].copy()
        if obj == 'all':
            titles = [outputs[i]['title'] for i in outputs]
            overall_progression = data[data['Country'] == 'All']['all'].values[0] / 144
            fig2 = indicateur([0, 100], ['0', '25%', '50%', '75%', '100%'], [0, 25, 50, 75, 100],
                              "Project's' overall completion (mean completion of all outputs)",
                              progression, overall_progression, retard(progression, overall_progression))
            for i in range(16):
                indic = country_coord.columns.tolist()[1:-1][i]
                progress = country_coord[indic].values[0]/9
                outputs_fig[i] = indicateur([0, 100], ['0', '25%', '50%', '75%', '100%'], [0, 25, 50, 75, 100],
                                          indic, progression, progress, retard(progression, progress))
            text_map = f'Overall progress of the project per indicator and country'

        else:
            titles = position_pays
            outcomes_styles = [{"display": "none"} for _ in range(6)]
            overall_progression = data[data['Country'] == 'All'][obj].values[0] / 800
            fig2 = indicateur([0, 100], ['0', '25%', '50%', '75%', '100%'], [0, 25, 50, 75, 100],
                              f'Project overall completion of objective {outputs[obj]["title"][:-1]} in {country}',
                              progression, overall_progression, retard(progression, overall_progression))
            for i in range(16):
                if position_pays[i] != '':
                    pays = position_pays[i]
                    progress = data[data['Country'] == pays][obj].values[0]
                    outputs_fig[i] = indicateur([0, 100], ['0', '25%', '50%', '75%', '100%'], [0, 25, 50, 75, 100],
                                                pays, progression, progress, retard(progression, progress))

                else:
                    styles[i] = {'visibility': 'hidden'}
            text_map = f'Overall progress of indicator: {outputs[obj]["title"][:-1]} per country'

    # ______________________________________ Carte ______________________________________________________ #

    with open('./maps/map_central_south_africa.json') as f:
        pays_map = json.load(f)

    carte2 = go.Figure(go.Choroplethmapbox(
        geojson=pays_map,
        featureidkey='properties.name',  # property of geoJSON file
        locations=countries['Country'],
        z=countries[obj],  # importing column consisting of
        zmin=0, zmax=10,  # active cases data
        autocolorscale=False,
        colorscale='Reds',
        marker_line_color='peachpuff', ))
    carte2.update_layout(mapbox_style="carto-positron",
                         mapbox_zoom=3, mapbox_center={"lat": -16.0902, "lon": 25.7129})
    carte2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    print(titles)

    return [fig2, carte2, 0, text_map]+outputs_fig+styles+titles+outcomes_styles


if __name__ == '__main__':
    app.run_server(debug=True)
