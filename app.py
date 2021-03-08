import dash as dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc



# Initial Bootstrap
# https://towardsdatascience.com/python-for-data-science-bootstrap-for-plotly-dash-interactive-visualizations-c294464e3e0e

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# creating data
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

colors = {'background':"#111111",'text':'#7FDBFF'}
scatterplot1 = dcc.Graph(id='scatterplot1',
                            figure = {'data':[
                                go.Scatter(
                                x=random_x,
                                y=random_y,
                                mode='markers',
                                marker = {
                                    'size':12,
                                    'color':'rgb(51,204,155)',
                                    'symbol':'pentagon',
                                    'line':{'width':2}
                                }
                                )],
                                'layout':go.Layout(title='Shorter Scatterplot')})

scatterplot2 = dcc.Graph(id='scatterplot2',
                                figure = {'data':[
                                    go.Scatter(
                                    x=random_x,
                                    y=random_y,
                                    mode='markers',
                                    marker = {
                                        'size':12,
                                        'color':'rgb(51,140,100)',
                                        'symbol':'pentagon',
                                        'line':{'width':2}
                                    }
                                    )],
                                    'layout':go.Layout(title='Longer Scatterplot')})

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
# defining navbar items
home_button = dbc.NavItem(dbc.NavLink('Home',href="#home", external_link=True,className='navlinks'))
statistic_button = dbc.NavItem(dbc.NavLink('Statistics',href="#statistics", external_link=True,className='navlinks'))
trend_button = dbc.NavItem(dbc.NavLink('Trend',href="#trend", external_link=True,className='navlinks'))
news_button = dbc.NavItem(dbc.NavLink('News',href="#news", external_link=True,className='navlinks'))


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
        dbc.Collapse(dbc.Nav([home_button,statistic_button,trend_button,news_button],className='ml-auto work-sans', navbar=True), id="navbar-collapse", navbar=True),
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
        html.H1("Jake Foose is a dingus", className="display-3"),
        html.P(
            "A deep dive into revenue for the year, segmented by verticals.",
            className="lead blue",
        ),
        html.Hr(className="my-2"),
        html.P(dbc.Button("Overview", color="primary"), className="lead"),
    ]
)


app.layout = html.Div(
    children = [
        navbar,
        jumbotron,
        html.Div(
            dbc.Row([
                        dbc.Col(html.Div("asdasd"), width=4),
                        dbc.Col(ridership_figure, width=8)
                    ]
                    )
                ,className = 'container'
            )
    ]
)

if __name__ == '__main__':
    app.run_server()