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
        style={ 'max-width': '85%'}
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

row1_text = "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."

row2_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

app.layout = html.Div(
    children = [
        navbar,
        html.Div(
            dbc.Row([
                dbc.Col( 
                    html.Div([
                                html.Hr(),
                                html.H1("Title: BLAH BLAH"),
                                html.P(row1_text),
                                html.Hr()
                            ]),
                 width=10)
                ]
            ), className='container'
        ),        
        html.Div(
            dbc.Row([
                        dbc.Col(
                            html.Div([
                                html.H2("SubTitle 1"),
                                html.P(row2_text),
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
                            html.P(row2_text),
                            html.Hr() 
                    ]), width = 4)
            ]), className='container'
        )

    ]
)



if __name__ == '__main__':
    app.run_server()