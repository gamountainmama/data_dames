import dash_bootstrap_components as dbc
from dash import html

def Navbar():
    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="/apps/home")),
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Rural School GA", href="/apps/app3"),
                        dbc.DropdownMenuItem("Private School FL", href="/apps/app2"),
                        dbc.DropdownMenuItem("Kaggle Data", href="/app1"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Education Stats",
                ),
                dbc.NavItem(dbc.NavLink("About", href="/pages/about")),
            ],
            brand="School Statistics",
            brand_href="/pages/home",
            style={"margin-bottom": 5},
            color="black",
            dark=True,
        )
    ])

    return layout
