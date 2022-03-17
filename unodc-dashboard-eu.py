import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from app import server
# import all pages in the app
from apps import map, indicators, home

# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
# dropdown = dbc.DropdownMenu(
#     children=[
#         dbc.DropdownMenuItem("Home", href="/home"),
#         dbc.DropdownMenuItem("Map", href="/map"),
#         dbc.DropdownMenuItem("Indicators", href="/indicators"),
#     ],
#     nav=True,
#     in_navbar=True,
#     label="Explore",
# )

#
button_group = dbc.ButtonGroup([dbc.Button("Home"), dbc.Button("Map"), dbc.Button("Indicators")])

# navbar = dbc.Navbar(
#             dbc.Container([dbc.Row(
#                         [dbc.Col(html.Img(src="/assets/EU.png", height="90px")),
#                          dbc.Col(dbc.NavbarBrand("PORT SECURITY AND SAFETY OF NAVIGATION "
#                                                         "IN EASTERN ANDSOUTHERN AFRICA AND THE INDIAN OCEAN"
#                                                         , className="ms-2")),
#                          dbc.Col(html.Img(src="/assets/UNODC.png", height="90px"))
#                         ],align="center",
#                         className="g-0"),
#                         #html.Img(src="/assets/UNODC.png", height="90px"),
#                         #dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
#                         button_group,
#                         html.Img(src="/assets/logoAxiom.png", height="90px"),
#                         ]),
#     color="dark",
#     dark=True,
#     className="m0   ",
# )

navbar = dbc.Nav(
    [
        dbc.NavItem(html.Img(src="/assets/EU.png", height="90px")),
        dbc.NavItem(html.Div([html.H3("Port Security and Safety of Navigation in ",style={'color':'white'}),
                            html.H3("Eastern and Southern Africa and the Indian Ocean",style={'color': 'white'})],
                             style={'display':'inline'} )),
        dbc.NavLink("LOGFRAME", href="/home",style={"font-size": "40"}),
        dbc.NavItem(dbc.NavLink("MAP", href="/map")),
        dbc.NavItem(dbc.NavLink("INDICATORS", href="/indicators")),
        dbc.NavItem(dbc.NavLink("OTHER DASHBOARD", href="https://axiommeltd11.shinyapps.io/UNODCDashboard/?_ga="
                                                        "2.152132607.713850576.1645610100-836082774.1645173603"
                                , target="_blank")),
        dbc.NavItem(html.A(html.Img(src="/assets/logoAxiom.png", height="90px"),href='https://axiom.co.ke/',
                           target="_blank")),
    ], class_name="navbar navbar-dark bg-dark")

# add callback for toggling the collapse on small screens
# @app.callback(
#     Output("navbar-collapse", "is_open"),
#     [Input("navbar-toggler", "n_clicks")],
#     [State("navbar-collapse", "is_open")],
# )
# def toggle_navbar_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Br(),
    html.Div(id='page-content',style={"display": "flex", "flex-direction": "column"})
],style={"display": "flex", "flex-direction": "column"})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/map':
        return map.layout
    elif pathname == '/indicators':
        return indicators.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)
