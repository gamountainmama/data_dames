import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import pathlib


'''This is the app for the excel evaluation of GA. '''


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

app4 = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Evaluation of Education Standards",
    url_base_pathname="/",
    suppress_callback_exceptions=False,
    assets_folder=str(DATA_PATH.joinpath("../assets").resolve())
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("School Statistics", href="/pages/home"),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/app"),
                    dbc.DropdownMenu(
                        [
                            dbc.DropdownMenuItem("Education Stats", header=True),
                            dbc.DropdownMenuItem("Rural School GA", href="http://127.0.0.1:8053/"),
                            dbc.DropdownMenuItem("Private School FL", href="http://127.0.0.1:8052/"),
                            dbc.DropdownMenuItem("Kaggle Data", href="http://127.0.0.1:8051/"),
                            dbc.DropdownMenuItem("Primitive Data Analysis", href="http://127.0.0.1:8054/"),
                        ],
                        in_navbar=True,
                        label="Education Stats",
                        color="secondary",
                    ),
                    dbc.NavLink("About", href="/pages/about"),
                ],
                className="ml-auto",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)

def layout4():
    return dbc.Container([
            navbar,
            html.H2("Analyzing On a Yearly Basis", style={"padding": "20px"}),
            html.P(
                '''Education demographics is a complex and multifaceted field with various 
                factors.Some issues with my previous experience include time constraints, 
                minimal visualizations, lack of timely analysis to help current students, 
                and my inability to assess the influence of various demographics. With machine 
                learning, we attempt to create models that will help predict the future 
                performance of students with similar demographics. Before Bootcamp, this is what 
                analysis of a rural Georgia school looked like using only Excel.'''
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(src='../assets/overall.png', alt="My Image", style={'width': '100%', 'height': 'auto'}),
                        width=6,
                        className="image-container"
                    ),
                    dbc.Col(
                        html.Img(src='../assets/plotted.png', alt="My Image", style={'width': '100%', 'height': 'auto'}),
                        width=6,
                        className="image-container"
                    ),
                    dbc.Col(
                        html.Img(src='../assets/spread.png', alt="My Image", style={'width': '100%', 'height': 'auto'}),
                        width=6,
                        className="image-container"
                    ),
                    dbc.Col(
                        html.Img(src='../assets/spread2.png', alt="My Image", style={'width': '100%', 'height': 'auto'}),
                        width=6,
                        className="image-container"
                    ),
                ],
                className="grid-container"
            ),
        ],
        style={"padding": "20px"},
        fluid=True
    )

app4.layout = layout4

if __name__ == "__main__":
    app4.run_server(port=8054, debug=True)

