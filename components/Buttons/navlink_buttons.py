import dash as dash
import dash_bootstrap_components as dbc

home_button = dbc.NavItem(
    dbc.NavLink('Home',
        href="#home", 
        external_link=True,
        className='navlinks'
        )
    )

city_map_button = dbc.NavItem(
    dbc.NavLink('City Map',
    href="#chimap", 
    to="https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-City/ewy2-6yfk",
    external_link=True,
    className='navlinks')
    )

city_bus_button = dbc.NavItem(
    dbc.NavLink('Trend',
    href="#trend",
    to="https://data.cityofchicago.org/browse?q=stops&sortBy=relevance",
    external_link=True,
    className='navlinks')
 )

news_button = dbc.NavItem(
    dbc.NavLink('EDA - Links',
    href="#news",
    to="https://www.google.com", 
    external_link=True,
    className='navlinks'))
