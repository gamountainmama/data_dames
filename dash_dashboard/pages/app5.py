import dash
import dash_bootstrap_components as dbc
import pathlib

from dash import dcc, html


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

app5 = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Evaluation of Education Standards",
    url_base_pathname="/",
    suppress_callback_exceptions=True
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

def layout5():
    layout = html.Div(
        [
            navbar,
            html.H1("Predictive Modeling in Education", className="display-4"),
            html.H2("About our Project", style={"padding": "10px"}),
            html.P('''In this project, we aim to compare and analyze the demographics and test scores of two different schools: a private wealthy school in Florida and a small rural school in Georgia. The two schools represent different socioeconomic backgrounds, and we can expect to observe significant differences in their student populations. We built a Neural Network model to predict the academic success of the students and determine if they will pass or fail their classes.''',
                        style={"padding": "10px","font-size": "21px"}
                    ),
            html.P('''Education involves a complex system with many factors that influence students outcomes. Factors such as demographics, test scores, socioeconomic status, and parental involvement are just some of the more obvious data points to consider. But there are many other points that can affect students success, social emotional health, motivation, personal circumstances, learning difficulties and even puberty.''',
                   style={"padding": "10px","font-size": "21px"}),
            html.Hr(className="my-4", style={"border-top": "2px solid #ccc"}),

            html.H2("About our Team", style={"padding": "10px"}),
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(html.P("Carol Love"), width=3,style={"font-size": "21px"}),
                            dbc.Col(html.P("Sahmirah Muhammad"), width=3,style={"font-size": "21px"}),
                            dbc.Col(html.P("Kendall Sanders"), width=3,style={"font-size": "21px"}),
                            dbc.Col(html.P("Kelly Schuster-Paredes"), width=3,style={"font-size": "21px"}),
                        ],
                        className="mt-2",
                    ),
                ],
                className="container",
            ),
            html.P(""),
            html.P(""),
            html.P(""),
            html.Hr(className="my-4", style={"border-top": "2px solid #ccc"}),

            html.H2("Throughout our project, we focused on answering the following questions:",
                    style={"padding": "10px"}),

            html.Div(
                [
                    html.Table(
                        [
                            html.Tbody(
                                [
                                    html.Tr(
                                        [
                                            html.Td('1:', style={"font-size": "21px"}),
                                            html.Td(
                                                "How can we use demographic information and past performance to predict academic success?",
                                                style={"font-size": "18px"}
                                            )
                                        ]
                                    ),
                                    html.Tr(
                                        [
                                            html.Td("2:", style={"font-size": "21px"}),
                                            html.Td(
                                                "Would it be possible to predict students' performance in midterms to help predict future grades?",
                                                style={"font-size": "18px"}
                                            )
                                        ]
                                    ),
                                    html.Tr(
                                        [
                                            html.Td("3.", style={"font-size": "21px"}),
                                            html.Td(
                                                "Could a program such as ours be used to identify at-risk students?",
                                                style={"font-size": "18px"}
                                            )
                                        ]
                                    ),
                                    html.Tr(
                                        [
                                            html.Td("4.", style={"font-size": "21px"}),
                                            html.Td(
                                                "How could we use data to identify the most influential factors contributing to academic success?",
                                                style={"font-size": "18px"}
                                            )
                                        ]
                                    ),
                                    html.Tr(
                                        [
                                            html.Td("5.", style={"font-size": "21px"}),
                                            html.Td(
                                                "Could we eventually extrapolate our model to identify success in higher education?",
                                                style={"font-size": "18px"}
                                            )
                                        ]
                                    ),
                                    html.Tr(
                                        [
                                            html.Td("6.", style={"font-size": "21px"}),
                                            html.Td(
                                                "Could we compare various sub-groups and their outcomes to identify potential disparities?",
                                                style={"font-size": "18px"}
                                            )
                                        ]
                                    )
                                ]
                            )
                        ],
                        style={"margin": "10px", "font-family": "Arial", "border-collapse": "collapse"},
                        className="table"
                    ),
                ],
            ),
        ]
    )
    return layout


app5.layout = layout5

if __name__ == '__main__':
    app5.run_server(port=8055, debug=True)
