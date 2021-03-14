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
    y="rides",
    title="Bus Ridership (2001 - 2019)",
    labels={"rides" : "Number of Rides ( in Millions )"}
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
        style={ 'max-width': '100%'}
        )  
    ])

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
    dbc.NavLink('Transportation Equity',
    href="https://www.metroplanning.org/work/project/47/subpage/2", 
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

problem_layout =  dbc.Card(
                                dbc.CardBody(
                                    [
                                        
                                        html.H4("The Problem: ", className="card-title"),
                                        dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem(
                                                    [
                                                        dbc.ListGroupItemHeading("CTA Ridership is declining"),
                                                        dbc.ListGroupItemText("From 2012 to 2019, annual rides have declined by about 77.5 million."),
                                                        dbc.ListGroupItemText("With the stresses on the system from the COVID-19 pandemic, ridership stands to decline even further.")
                                                    ]
                                                ),
                                                dbc.ListGroupItem(
                                                    [
                                                        dbc.ListGroupItemHeading("City Hall has stopped supporting its public transportation"),
                                                        dbc.ListGroupItemText("The share of Chicago’s sales tax going to public transit has been cut in several of the past city budgets"),
                                                        dbc.ListGroupItemText("Taxes ostensibly designed to fund public transit have had a pitiful percentage earmarked for the CTA")
                                                    ]
                                                ),
                                                dbc.ListGroupItem(
                                                    [
                                                        dbc.ListGroupItemHeading("Chicago’s citizens do not choose to use public transit"),
                                                        dbc.ListGroupItemText("Chicago has not adequately proved to its citizens that the CTA is clean and safe in the wake of the COVID-19 pandemic."),
                                                        dbc.ListGroupItemText("30% of Chicago’s citizens live in Economically Disconected Areas where public transit is not even an option.")
                                                    ]
                                                )
                                            ]
                                            )
                                    ]
                                ),
                                style={"width": "100%", "height":"100%"},
                            )

solution_layout =  dbc.Card(
                                dbc.CardBody(
                                    [
                                        
                                        html.H4("Our Solution: ", className="card-title"),
                                        dbc.ListGroup(
                                            [
                                                dbc.ListGroupItem(
                                                    [
                                                        dbc.ListGroupItemHeading("Establish dedicated funding streams for the CTA through local taxes."),
                                                        dbc.ListGroupItemText("Earmark the entirety of Chicago’s rideshare tax earnings to the equitable development of the CTA."),
                                                        dbc.ListGroupItemText("Establish a local gas tax to both disincentivize driving in the city and encourage the increased use of public transit.")
                                                    ]
                                                ),
                                                dbc.ListGroupItem(
                                                    [
                                                        dbc.ListGroupItemHeading("Build 50 miles of bus lanes throughout the city"),
                                                        dbc.ListGroupItemText("Cities like Seattle, Los Angeles, and Denver have made buses faster and more reliable by instituting dedicated bus lanes throughout their cities."),
                                                        dbc.ListGroupItemText("Chicago can target these bus lanes to alleviate the inequities inherent in its 'Economically Disconnected Areas.'")
                                                    ]
                                                ),
                                                dbc.ListGroupItem(
                                                    [
                                                        dbc.ListGroupItemHeading("Begin a public education campaign focused on 'Equitable Transportation'"),
                                                        dbc.ListGroupItemText("A public education campaign will make more of Chicago’s citizens feel safe using the bus, helping spur a return to ridership."),
                                                        dbc.ListGroupItemText("With support of racial equity and social justice form, implementation will be both popular and effective.")
                                                    ]
                                                )
                                            ]
                                            )
                                    ]
                                ),
                                style={"width": "100%", "height":"100%"},
                            )

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
                                html.H1("P.S. I Bus You", className="display-2"),
                                html.P(
                                    "How to fix an unsupported system of transportation and reconnect disconnected communities",
                                    className="lead",
                                ),
                                html.Hr(),
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
                          problem_layout, width=8),
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
                            html.H6(
                                "A survey of individuals making $25,000 or less conducted by the Active Transportation Alliance found that 80% of respondents use the public transportation system to access their job. It is the people who rely on the public transportation system the most that are the most underserved. The City of Chicago has left over 30% of its citizens trapped without the means to help themselves."
                                , className="card-text lead"))
                        ), width=12
                    )]
                ), className='container', style={"max-width":"90%"}
            ),
        html.Hr(),
        html.Div(
            dbc.Row(
                [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(illinois_map_figure)
                        ), width = 4
                    ),
                dbc.Col(
                           solution_layout, 
                           width= 8 
                           )
                ]), 
            className='container', 
            style={"max-width":"90%"}),
        html.Hr(),
        html.Div(
            dbc.Row(
                [dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            html.H6(
                                "By utilizing this money, Denver’s rail ridership has gone up, Los Angeles is considering making their public transit free, and Seattle’s public transit system has seen years of rapid growth. Chicago, on the other hand, has been reducing the proportion of sales tax being used for public transit for the past several years, deferring maintenance and capital improvement projects. If Chicago is serious about improving its transit system, it should improve the funding streams it has, implement new ones, and then commit to using that money for public transit.",
                                className="card-text lead")
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


