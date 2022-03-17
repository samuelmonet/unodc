import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html, dash_table, dcc, callback, Input, Output
import datetime
import json

# --------------------------------- Definition tableau -------------------------------------------------- #

table={'Specific Objective(s)':
           ["Outcome 1.1", "Output 1.1.1", "Output 1.2.6", "Outcome 2.1", "Outcome 2.2", "Output 2.2.5"],
       'Expected Results':
           ["Reinforcement of the capacities of Maritime Affairs Authorities and governmental agencies.",
        "Identification of obstacles hampering the transposition of international main agreements "
        "and legislations into national legislation.",
        "Improved capacity building on Port State Control measures in relation to criminality aspects"
        " such as standard operating procedures, communications procedures, personnel security and so on.",
        "Implementation of ISPS Code and related compliance framework adopted by ports of the EA-SA-IO region.",
        "Develop and support the implementation of Port security management in the EA-SA-IO Region.",
        "Implementation of a cargo targeting system for risky consignments to enhance customs clearance"
        " of goods as prescribed by international best practices."],
        'Indicators':
       ["(6) Number of effective reviews of national legislation related to port security and "
        "maritime safety management completed. <br>(7) Number of proposals for adaption to national legislation. "
        "<br>(8) Number of personnel from judicial stakeholders trained on ensuring a legal finish to prosecutions "
        "of port related crimes. <br>(9) An initiation or increase in the number of prosecutions related to port"
        " safety and security measures. ",
        "(10) Number of obstacles found that hamper the transposition of international main agreements and "
        "legislations into national legislation.",
        "(22) Number of participants in training on the related subjects. <br>"
        "(23) Number of cases prosecuted in accordance with maritime legislation.",
        "(24) Number of ports having implemented the ISPS code and related regulatory compliance frameworks.",
        "(30) Number of  port or port facility security assessments completed. <br>(31) Number of Port Security "
        "Plans developed and implemented. <br>(32) Number of port staff trained in security, risk and incident "
        "management. <br>(33) Status of contingency plans and evacuation plans for different emergency "
        "situations/threats. <br>(34) Status of risk assessment for the ports facililites. <br>(35) Number of emergency "
        "exercises conducted with the support of this Action (disaggregated per country). <br>(36) Number of port "
        "security drills and exercises developed and delivered. ",
        "(40) Number of Port Comtrol Unit established in EA-SA-IO Region"],
       'Targets':
       [[9,9,27,9],
        ['unclear'],
        [27,9],
        ['unclear'],
        ['unknown','unknown',90,'unknown','unknown','unknown','unknown'],
        [9]],
        'Baseline':
        [['unclear','unclear','unclear','unclear'],
        ['unclear'],
        ['unclear','unclear'],
        ['unclear'],
        ['unclear','unclear','unclear','unclear','unclear','unclear','unclear'],
        [6]]}

table['Achievement']=[['16%','15%','16%','14%'],['16%'],['14%','15%'],['16%'],
                      ['14%','14%','15%','15%','17%','15%','16%'],['14%']] # List to update with achievements

# ______________________________________________________ Layout  _____________________________________________________ #

layout = [html.Br(),
          html.Div(html.H1("Summary of the project"),
                                style={"text-align": "center"}),    # Title
          html.Br(),
          html.Div(id='table',
                    children=[html.Div(id='features',
                                       children=[html.Div(style={"width":"3%"}),
                                                 html.Div( children=html.H5('Specific Objective(s)'),
                                                            style={"border-style": "solid","width":"6%",
                                                                   "border-right":None,'background-color':'blue',
                                                                   'color':'white','border-color':'black',
                                                                   'text-align':'center'}),
                                                html.Div( children=html.H5('Expected Results'),
                                                            style={"border-style": "solid","width":"20%",
                                                                   "border-right":None,'background-color':'blue',
                                                                   'color':'white','border-color':'black',
                                                                   'text-align':'center'}),
                                                html.Div( children=html.H5('Indicator(s)'),
                                                            style={"border-style": "solid","width":"47%",
                                                                   "border-right":None,'background-color':'blue',
                                                                   'color':'white','border-color':'black',
                                                                   'text-align':'center'}),
                                                html.Div( children=html.H5('Target'),
                                                            style={"border-style": "solid","width":"7%",
                                                                   "border-right":None,'background-color':'blue',
                                                                   'color':'white','border-color':'black',
                                                                   'text-align':'center'}),
                                                html.Div( children=html.H5('Baseline'),
                                                            style={"border-style": "solid","width":"7%",
                                                                   "border-right":None,'background-color':'blue',
                                                                   'color':'white','border-color':'black',
                                                                   'text-align':'center'}),
                                                html.Div( children=html.H5('Achievements (tentative figures)'),
                                                            style={"border-style": "solid","width":"7%",
                                                                   'background-color':'blue',
                                                                   'color':'white','border-color':'black',
                                                                   'text-align':'center'}),
                                                html.Div(style={"width": "3%"})],
                                       style={"display":'flex'})] +
                            [html.Div(id=table['Specific Objective(s)'][k],
                                      style={'display':'flex'},
                                      children=[html.Div(style={"width":"3%"}),
                                                html.Div(html.P(table['Specific Objective(s)'][k]),
                                                style={"border-style": "solid","width":"6%",
                                                        "border-top":None,"border-right":None,
                                                       'background-color':'lightblue',}),
                                                html.Div(html.P(table['Expected Results'][k]),
                                                         style={"border-style": "solid","width":"20%",
                                                                "border-top":None,"border-right":None}),
                                                html.Div([html.P(k) for k in table['Indicators'][k].split('<br>')],
                                                         style={"border-style": "solid","width":"47%",
                                                                "border-top":None,"border-right":None}),
                                                html.Div([html.P(k) for k in table['Targets'][k]],
                                                         style={"border-style": "solid","width":"7%",
                                                                "border-top":None,"border-right":None,
                                                                'text-align':'center'}),
                                                html.Div([html.P(k) for k in table['Baseline'][k]],
                                                         style={"border-style": "solid","width":"7%",
                                                                "border-top":None,"border-right":None,
                                                                'text-align':'center'}),
                                                html.Div([html.P(k) for k in table['Achievement'][k]],
                                                         style={"border-style": "solid","width":"7%",
                                                                "border-top":None,'text-align':'center'}),
                                                html.Div(style={"width":"3%"}),])
                             for k in range(6) ],
                            style={"display":'flex','flex-direction':'column'}),
        html.Br(),
        html.P('Unclear and Unknown means that I did not manage to understand the targets or the baseline from the excelsheet'),
          # html.Div(id='table',
          #          children=[html.Div(id=feature,
          #
          #                             children=[html.Div(html.H5(feature),style={"border-style": "solid"})]+
          #                                       [html.Div([html.P(line) for line in table[feature][k].split('<br>')],
          #                                                 style={"border-style": "solid"}) for k in range(6)]
          #                               ,style={"display":'flex','flex-direction':'column'}) for feature in table],
          #           style={"display":'flex'}),

        ]




#
# @callback([Output(component_id='objective_target', component_property='figure'),
#                Output(component_id='carte2', component_property='figure'),
#                Output(component_id='carte', component_property='n_clicks'),
#                Output(component_id='text_map', component_property='children')] +
#             [Output(component_id=i, component_property='figure') for i in names] +
#             [Output(divs[i], 'style') for i in range(16)]+[Output(divs[i], 'title') for i in range(16)] +
#             [Output(component_id='outcome'+str(i), component_property='style') for i in range(1, 7)],
#             [Input(component_id="select_obj", component_property='value'),
#              Input('carte', 'n_clicks'), Input('carte2', 'clickData')])
# def update_graphs(obj, clicks, what):
#     #print('What ', what)
#     #print('clicks ', clicks)
#     #print('obj', obj)
#     # Liste indicateurs
#     fig6 = fig7 = fig8 = fig9 = fig10 = fig22 = fig23 = fig24 = fig30 = fig31 = fig32 = fig33 = fig34 = fig35 = fig36 =\
#         fig40 = go.Figure()
#     outputs_fig = [fig6, fig7, fig8, fig9, fig10, fig22, fig23, fig24, fig30, fig31, fig32, fig33, fig34, fig35, fig36,
#                fig40]
#     styles = [{} for _ in range(16)]
#     outcomes_styles = [{} for _ in range(6)]
#     position_pays = ['', 'Angola', 'Namibia', '', '', '', '', 'Mozambique', 'Kenya', 'Seychelles', 'Tanzania',
#                      'Madagascar', 'Mauritius', '', '', 'Comoros']
#
#     if clicks != 0:
#         what = None
#
#     if what is not None:
#
#         country = what['points'][0]['location']
#         country_coord = data[data['Country'] == country].copy()
#         countries = data[data['Country'] == country].copy()
#         overall_progression = country_coord['all'].values[0] / 18
#         fig2 = indicateur([0, 100], ['0', '25%', '50%', '75%', '100%'], [0, 25, 50, 75, 00],
#                           f'Project overall completion in {country}', progression,
#                         overall_progression, retard(progression, overall_progression))
#         #print(country)
#         #print(country_coord)
#
#         if obj == 'all':
#             titles = [outputs[i]['title'] for i in outputs]
#             for i in range(16):
#                 indic = data.columns.tolist()[1:-1][i]
#                 progress = country_coord[indic].values[0]
#
#                 outputs_fig[i] = indicateur(outputs[indic]['range'], outputs[indic]['ticktext'],
#                                             outputs[indic]['tickval'], indic, progression, progress,
#                                             retard(progression, progress))
#             text_map = f'Different indicators completion in {country} since the beginning of the project'
#
#         else:
#             titles = position_pays
#             progress = country_coord[obj].values[0]
#             outcomes_styles = [{"display": "none"} for _ in range(6)]
#             for i in range(16):
#                 if position_pays[i] == country:
#                     outputs_fig[i] = indicateur(outputs[obj]['range'], outputs[obj]['ticktext'],
#                                                 outputs[obj]['tickval'], obj, progression, progress,
#                                                 retard(progression, progress))
#
#                 else:
#                     outputs_fig[i] = indicateur(outputs[obj]['range'], outputs[obj]['ticktext'],
#                                                 outputs[obj]['tickval'], obj,
#                                                 progression, progress, retard(progression, progress))
#                     styles[i] = {"visibility": "hidden"}
#             text_map = f'Completion of indicator: {outputs[obj]["title"]}'
#
#     # indicateur(range, ticktext, tickval, title, progression_temps, progression_objectif, couleur)
#
#     else:
#         country = 'All'
#         countries = data.drop([9], axis=0).copy()
#         country_coord = data[data['Country'] == country].copy()
#         if obj == 'all':
#             titles = [outputs[i]['title'] for i in outputs]
#             overall_progression = data[data['Country'] == 'All']['all'].values[0] / 144
#             fig2 = indicateur([0, 100], ['0', '25%', '50%', '75%', '100%'], [0, 25, 50, 75, 100],
#                               "Project's' overall completion (mean completion of all outputs)",
#                               progression, overall_progression, retard(progression, overall_progression))
#             for i in range(16):
#                 indic = country_coord.columns.tolist()[1:-1][i]
#                 progress = country_coord[indic].values[0]/9
#                 outputs_fig[i] = indicateur([0, 100], ['0', '25%', '50%', '75%', '100%'], [0, 25, 50, 75, 100],
#                                           indic, progression, progress, retard(progression, progress))
#             text_map = f'Overall progress of the project per indicator and country'
#
#         else:
#             titles = position_pays
#             outcomes_styles = [{"display": "none"} for _ in range(6)]
#             overall_progression = data[data['Country'] == 'All'][obj].values[0] / 800
#             fig2 = indicateur([0, 100], ['0', '25%', '50%', '75%', '100%'], [0, 25, 50, 75, 100],
#                               f'Project overall completion of objective {outputs[obj]["title"][:-1]} in {country}',
#                               progression, overall_progression, retard(progression, overall_progression))
#             for i in range(16):
#                 if position_pays[i] != '':
#                     pays = position_pays[i]
#                     progress = data[data['Country'] == pays][obj].values[0]
#                     outputs_fig[i] = indicateur([0, 100], ['0', '25%', '50%', '75%', '100%'], [0, 25, 50, 75, 100],
#                                                 pays, progression, progress, retard(progression, progress))
#
#                 else:
#                     styles[i] = {'visibility': 'hidden'}
#             text_map = f'Overall progress of indicator: {outputs[obj]["title"][:-1]} per country'
#
#     # ______________________________________ Carte ______________________________________________________ #
#
#     with open('./maps/map_central_south_africa.json') as f:
#         pays_map = json.load(f)
#
#     carte2 = go.Figure(go.Choroplethmapbox(
#         geojson=pays_map,
#         featureidkey='properties.name',  # property of geoJSON file
#         locations=countries['Country'],
#         z=countries[obj],  # importing column consisting of
#         zmin=0, zmax=10,  # active cases data
#         autocolorscale=False,
#         colorscale='Reds',
#         marker_line_color='peachpuff'))
#     carte2.update_layout(mapbox_style="carto-positron",
#                          mapbox_zoom=3, mapbox_center={"lat": -16.0902, "lon": 25.7129})
#     carte2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
#
#     #print(titles)
#
#     return [fig2, carte2, 0, text_map]+outputs_fig+styles+titles+outcomes_styles
#
#
