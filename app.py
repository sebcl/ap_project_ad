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
# print(cta_bus_ridership)
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

#%%

test_map = gpd.read_file("./Boundaries - City/geo_export_b127f319-53a1-4af3-924f-5b23c29c095c.shp")

test_map

#%%

# def read_shp( import_sf ):
 #   # Take in shapefile and hopefully spit something out
    # No error handling - YOLO

#    fields = [col[0] for col in import_sf.fields][1:]
#    records = import_sf.records()
#    sf_shapes = [s_sh.points for s_sh in import_sf.shapes()]

#    shapes_df = pd.DataFrame(columns = fields, data = records)
#    shapes_df = shapes_df.assign(coords=sf_shapes)
    
#    return shapes_df

# def shape_shp_dataframe( df_to_plot, df_id, s=None):
    # Take in dataframe and spit out matplot geo 
    # No error handling - YOLO
 #   plt.figure()
 #   ax = plt.axes()
  #  ax.set_aspect('equal')
   # shape_ex = df_to_plot.shape(id)
  #  x_lon = np.zeros((len(shape_ex.points),1))
   # y_lat = np.zeros((len(shape_ex.points),1))

 #   for ip in range(len(shape_ex.points)):
 #       x_lon[ip] = shape_ex.points[ip][0]
 #       y_lat[ip] = shape_ex.points[ip][1]    
        
 #   plt.plot(x_lon,y_lat) 
  #  x0 = np.mean(x_lon)
   # y0 = np.mean(y_lat)
    #plt.text(x0, y0, s, fontsize=10)
    # use bbox (bounding box) to set plot limits
    #plt.xlim(shape_ex.bbox[0],shape_ex.bbox[2])
    #return x0, y0



# city_chicago = shp.Reader("./Boundaries - City/geo_export_b127f319-53a1-4af3-924f-5b23c29c095c.shp")
# bus_stops = shp.Reader("./CTA_BusStops/CTA_BusStops.shp")

#test2 = shape_shp_dataframe(bus_stops, )
#cta_busstops = pd.read_csv("CTA_BusStops.csv")
#fig = px.scatter_geo(cta_busstops,
#lat='POINT_X',
#lon='POINT_Y')
#
#fig.update_layout(
#        title = 'Most trafficked US airports<br>(Hover for airport names)',
#        geo_scope='illinois',
#    )
#
#fig.show()
#
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
                dbc.Col(ridership_figure_temp, width = 8),
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