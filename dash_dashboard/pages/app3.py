import dash
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib
import plotly.express as px
from dash import dcc, html, Input, Output

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
EXAMS_CSV_PATH = DATA_PATH.joinpath("ga_data_overall_success.csv")

GAdemographics_df = pd.read_csv(EXAMS_CSV_PATH)

app3 = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Evaluation of Education Standards",
    url_base_pathname="/",
    suppress_callback_exceptions=True,
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


def layout3():
    layout = html.Div(
        dbc.Container(
            [
                navbar,
                html.H1("Georgia Rural School", style={"padding": "10px"}),
                html.P(
                    '''The Georgia Milestones data uses the following features: 
                    gender, ethnicity, English-language learners (ELL), students with 
                    disabilities (SWD), economic disadvantage (ED), student support team (ST), 
                    gifted, absences, Lexile level, and previous year’s scores.\n

                    Acronym Key:
                    ELL (English Language Learner),
                    SWD (Student with Disability),
                    ED (Economically Disadvantaged),
                    SST (Student Support Team),
                    Lexile (Measure of reading ability), 
                    Achievement Levels: [
                    1 - Beginning Learner (failing)
                    2 - Developing Learner
                    3 - Proficient Learner
                    4 - Distinguished Learner]
                    ''',
                    style={"padding": "10px"}
                ),
                html.H3("Neural Network Model", style={"padding": "10px"}),
                html.P(
                            '''
                            We created a neural network model with two layers as shown on the left.\n

                            The Georgia Milestones data uses the following features: gender, ethnicity, English-language learners (ELL), 
                            students with disabilities (SWD), economic disadvantage (ED), student support team (ST), gifted, absences, 
                            Lexile level, and previous year’s scores.
                            ''',
                            style={"padding": "40px"}
                        ),
                html.Div(
                    [
                        html.Img(src='../assets/neural.png', alt="My Image", style={'width': '90%', 'height': '60%'}),
                        html.A(
                            html.Img(src='../assets/ga_tableau.png', alt="My Image", style={'width': '90%', 'height': '70%','padding-left': '10px'}),
                            href="https://public.tableau.com/app/profile/sahmirah.muhammad/viz/RuralGAPublicSchoolData/Story1",
                            target="_blank"
                        ),

                        
                    ],
                    style={"display": "flex", "justify-content": "center"}
                ),
                html.Div(
                    [   
                        html.P(''),
                        html.P(''),
                        html.H3("Accuracy Results and Feature Ranking for Georgia Milestones"),
                        html.Img(src='../assets/ga_features.png', alt="My Image", style={'width': '50%', 'height': '30%'}),
                        html.Div(
                            [
                                html.Table(
                                    [
                                        html.Thead(
                                            html.Tr([html.Th("Test"), html.Th("Accuracy")])
                                        ),
                                        html.Tbody(
                                            [
                                                html.Tr([html.Td("English Language Arts (ELA)"), html.Td("0.867")]),
                                                html.Tr([html.Td("Math (MATH)"), html.Td("0.933")]),
                                                html.Tr([html.Td("Science (SCIE)"), html.Td("0.667")]),
                                                html.Tr([html.Td("Social Studies (SOCI)"), html.Td("0.900")]),
                                                html.Tr([html.Td("Overall (Passing all four tests)"), html.Td("0.833")])
                                            ]
                                        ),
                                    ],
                                    style={"margin": "10px"},

                                )
                            ],
                            className="col-md-5"
                        ),
                        
                    ],
                    className="row"

                ),
                dcc.Dropdown(
                    id="student-dropdown2",
                    options=[
                        {"label": student_id, "value": student_id}
                        for student_id in GAdemographics_df["Overall Pass"]
                    ],
                    value=GAdemographics_df["Overall Pass"].iloc[0]
                ),
                dcc.Graph(id="scatter_plot_data2"),
            ],
            fluid=True,
        )
    )
    return layout


@app3.callback(
    Output("scatter_plot_data2", "figure"),
    Input("student-dropdown2", "value"),
)
def update_student_data3(ethnicity):
    scatter_data3 = px.scatter(
        GAdemographics_df,
        x="MATH 21 Scale Score",
        y="ELA 21 Scale Score",
        color="Gender",
        template="plotly_dark",
        labels={"Gender": "Gender"},
        hover_data=GAdemographics_df.columns,
        title="Math versus Reading per Gender",
    )
    return scatter_data3


app3.layout = layout3

if __name__ == '__main__':
    app3.run_server(port=8053, debug=True)
