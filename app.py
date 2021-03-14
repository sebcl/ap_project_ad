import dash as dash
import dash_core_components as dcc
import dash_html_components as html
import geopandas as gpd
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
import base64
# import mkl

# from components import home_button, news_button, city_bus_button, city_map_button 


# Functions

# Initial Bootstrap
# https://towardsdatascience.com/python-for-data-science-bootstrap-for-plotly-dash-interactive-visualizations-c294464e3e0e

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
# defining navbar items


## Data - Bus Ridership
cta_bus_ridership = pd.read_csv("CTA_-_Ridership_-_Bus_Routes_-_Daily_Totals_by_Route.csv")
cta_bus_ridership['Year'] = pd.DatetimeIndex(cta_bus_ridership['date']).year
# Drop 2020
cta_bus_ridership.drop(
    cta_bus_ridership[cta_bus_ridership['Year']==2020].index, inplace=True
)  
annual_cta_ridership = cta_bus_ridership.groupby('Year').sum()
# print(annual_cta_ridership)

ridership_graph = px.scatter(
    annual_cta_ridership,
    x=annual_cta_ridership.index,
    y="rides"
)

ridership_graph.update_layout(clickmode='event+select')
ridership_graph.update_traces(marker_size=20)

ridership_figure = html.Div([
    dcc.Graph(
        id="ridership",
        figure=ridership_graph
    )
])


# Save For Later - Just utilze the png version of the bus stops :( 

    # test_map = gpd.read_file("./Boundaries - City/geo_export_b127f319-53a1-4af3-924f-5b23c29c095c.shp")
    # chi_bus_stops = gpd.read_file("./CTA_BusStops/CTA_BusStops.shp")
    # chi_bus_stopMap = chi_bus_stops.plot(figsize=(30,30), markersize=2)
    # chi_bus_stopMap.set_axis_off()

# Image of Bus Stops - Update to filter for certain routes?
busStopsImage = 'chi_busStops.png' # replace with your own image
encoded_busStopImage = base64.b64encode(open(busStopsImage, 'rb').read())

illinois_map_figure = html.Div([
    html.Img(
        src='data:image/png;base64,{}'.format(encoded_busStopImage.decode()),
        style={ 'max-width': '90%'}
        )  
    ])

home_button = dbc.NavItem(
    dbc.NavLink('Home',
        href="#home", 
        external_link=True,
        className='navlinks'
        )
    )

city_map_button = dbc.NavItem(
    dbc.NavLink('City Map',
    href="https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-City/ewy2-6yfk",
    external_link=True,
    className='navlinks')
    )

city_bus_button = dbc.NavItem(
    dbc.NavLink('Trend',
    href="https://data.cityofchicago.org/browse?q=stops&sortBy=relevance",
    external_link=True,
    className='navlinks')
 )

news_button = dbc.NavItem(
    dbc.NavLink('EDA - Links',
    href="https://www.google.com", 
    external_link=True,
    className='navlinks'))

ridership_figure_temp = html.Div([
    dcc.Graph(
        id="ridership2",
        figure=ridership_graph
    )
])


navbar = dbc.Navbar(
    dbc.Container(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                   dbc.Col(dbc.NavbarBrand("Analytical Politics II", className="ml-2 work-sans")),
                ],
                align="left",
                no_gutters=True,
            ),
            href="#home",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(
            dbc.Nav(
                [
                    home_button,
                    city_map_button,
                    city_bus_button,
                    news_button
                    ],className='ml-auto work-sans', navbar=True), id="navbar-collapse", navbar=True),
    ],
    ),
    color="rgb(42,62,66)",
    dark=True,
    style = {'background-color':'#191919'},
    className = 'navbar-change',
    expand= 'lg'   
)

group_info = dbc.Row(
    [
     
     dbc.Col([
    dbc.Card(
    dbc.ListGroup(
        [
            dbc.ListGroupItem("Joe Kensok"),
            dbc.ListGroupItem("Jake Foose"),
            dbc.ListGroupItem("Aidan Coffey"),
            dbc.ListGroupItem("Sebastian Clavijo")
        ],
        flush=True, className="align-self-center h-50"
    ),
    style={"width": "100%"}, className="align-self-center h-50"
)
])], align="center"
    )

row1_text = "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."

row2_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

app.layout = html.Div(
    children = [
        navbar,
        html.Div(
            dbc.Row([
                dbc.Col( 
                    dbc.Jumbotron(
                    [
                        dbc.Container(
                            [
                                html.H1("P.S. I bus you", className="display-3"),
                                html.P(
                                    "How to fix an unsupported system of transportation and reconnect disconnected communities",
                                    className="lead",
                                ),
                                html.P(
                                    "Identify funding streams to provide accessible and efficient bus transportation",
                                    className="lead",
                                ),
                                html.Br(),
                                html.H6("by: Sebastian Clavijo, Aidan Coffey, Joe Kensok, Jake Foose")
                            ],
                            fluid=True,
                        )
                    ],
                    fluid=True,
                ),
                 width=10)
                ]
            ), className='container', style={"max-width":"90%"}
        ),        
        html.Div(
            dbc.Row([
                        dbc.Col(
                           dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H4("The Problem: ", className="card-title"),
                                        html.P(
                                            "",
                                            className="card-text",
                                        ),
                                        dbc.CardLink("External link", href="https://google.com"),
                                    ]
                                ),
                                style={"width": "100%", "height":"100%"},
                            ), width=8),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [ridership_figure]
                                    )
                                ), 
                            width=4)
                    ]
                    )
                ,className = 'container', style={"max-width":"90%"}
        ),
        html.Hr(),
        html.Div(
            dbc.Row(
                [dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            html.P(
                                "A survey of individuals making $25,000 or less conducted by the Active Transportation Alliance found that 80% of respondents use the public transportation system to access their job. It is the people who rely on the public transportation system the most that are the most underserved. The City of Chicago has left over 30% of its citizens trapped without the means to help themselves."
                                , className="card-text"))
                        ), width=12
                    )]
                ), className='container', style={"max-width":"90%"}
            ),
        html.Hr(),
        html.Div(
            dbc.Row([
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                    illinois_map_figure        
                            )
                        ), width = 4),
                dbc.Col(
                           dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H4("Our Solution: ", className="card-title"),
                                        html.P(
                                            "",
                                            className="card-text",
                                        ),
                                        dbc.CardLink("External link", href="https://google.com"),
                                    ]
                                ),
                                style={"width": "100%", "height":"100%"},
                            ), width= 8 )
            ]
                    ), className='container', style={"max-width":"90%"}
        ),
        html.Hr(),
        html.Div(
            dbc.Row(
                [dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            html.P(
                                "By utilizing this money, Denver’s rail ridership has gone up, Los Angeles is considering making their public transit free, and Seattle’s public transit system has seen years of rapid growth. Chicago, on the other hand, has been reducing the proportion of sales tax being used for public transit for the past several years, deferring maintenance and capital improvement projects. If Chicago is serious about improving its transit system, it should improve the funding streams it has, implement new ones, and then commit to using that money for public transit.",
                                className="card-text")
                            )
                        ), width=12
                    )]
                ), className="container", style={"max-width":"90%"}
            ),
        html.Hr(),
    ]
, style={"background-color": "#e9ecef"})



if __name__ == '__main__':
    app.run_server()