import dash as dash
import dash_core_components as dcc
import dash_html_components as html
import geopandas as gpd
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
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


test_map = gpd.read_file("./Boundaries - City/geo_export_b127f319-53a1-4af3-924f-5b23c29c095c.shp")

chi_bus_stops = gpd.read_file("./CTA_BusStops/CTA_BusStops.shp")

chi_bus_stopMap = chi_bus_stops.plot(figsize=(30,30), markersize=2)
chi_bus_stopMap.set_axis_off()

illinois_map_figure = html.Div([
    dcc.Graph(
        id='bus_stops',
        figure = chi_bus_stopMap
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
                    dbc.Col(html.Img(src=PLOTLY_LOGO,className = 'logo',height="30px")),
                   dbc.Col(dbc.NavbarBrand("Analytical Politics", className="ml-2 work-sans")),
                ],
                align="center",
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

jumbotron = dbc.Jumbotron(
    [
        html.H1("Title", className="display-3"),
        html.P(
            "A deep dive into revenue for the year, segmented by verticals.",
            className="lead blue",
        ),
        html.Hr(className="my-2")
    ]
)

app.layout = html.Div(
    children = [
        navbar,
        jumbotron,
        html.Div(
            dbc.Row([
                        dbc.Col(
                            html.Div([
                                html.H2("SubTitle 1"),
                                html.P(""),
                                html.Hr()
                            ]
                            ), width=4),
                        dbc.Col(
                            ridership_figure, 
                            width=8)
                    ]
                    )
                ,className = 'container'
        ),
        html.Div(
            dbc.Row([
                dbc.Col(
                    illinois_map_figure,
                    width = 8),
                dbc.Col(
                    html.Div([
                       html.H2("SubTitle 2"),
                            html.P(""),
                            html.Hr() 
                    ]), width = 4)
            ]), className='container'
        )

    ]
)

if __name__ == '__main__':
    app.run_server()