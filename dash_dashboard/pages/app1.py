import dash
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib
import plotly.express as px
from dash import dcc, html, Input, Output
from flask import Flask, url_for

'''This is the app for the Kaggle Data.'''

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
EXAMS_CSV_PATH = DATA_PATH.joinpath("exams.csv")

demographics_df = pd.read_csv(EXAMS_CSV_PATH)
demographics_df.reset_index(inplace=True)
demographics_df.rename(
    columns={
        'index': 'student_id',
        'race/ethnicity': 'race_ethnicity',
        'parental level of education': 'parent_education'
    },
    inplace=True
)

app1 = dash.Dash(
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

def layout1():
   layout = html.Div(
        dbc.Container(
            [
                navbar,
            dbc.Container([
            html.Div([
                html.H1("Predictive Modeling in Education",className="display-4"),
                html.H2("Kaggle Synthetic School Data", style={"padding": "10px"}),

                html.P(
                    "Education demographics is a complex and multifaceted field with various factors such as test scores, financial incomes, gender, race, ethnicity, "
                    "school location, and parental education levels. This area of study has many problems that can make it difficult to obtain accurate and reliable data."
                    "Here are three key problems in education demographics:",
                    style={"font-size": "21px"}),
                    html.Ul([
                            html.Li(
                                '''Lack of standardized data collection methods: Different educational institutions and organizations may use different methods to collect data, 
                                leading to inconsistencies and difficulties in comparing and analyzing the information.''', 
                                style={"font-size": "21px"}),
                            html.Li(
                                '''Data privacy concerns: Education demographics often involve sensitive information about students and their families. Ensuring data privacy and 
                                security while still extracting valuable insights can be challenging.''',
                                style={"font-size": "21px"}),
                            html.Li(
                                "Limited representation: Some demographic groups may be underrepresented or overlooked in education data, leading to biased analyses and inadequate policy decisions.", style={"font-size": "21px"}), ],
                        className="custom-list",),],
                className="jumbotron",),
            dbc.Row([
                dbc.Col(
                    [
                        html.Img(src='../assets/kaggle_features.png', alt="My Image", style={'width': '100%', 'height': '60%'}),
                
                    ],
                    width=6
                ),
                    dbc.Col([
                        html.H2("Kaggle Data", className="display-5"),
                        html.Div([
                            html.Table([
                                html.Thead(
                                    html.Tr([html.Th("Attribute"), html.Th("Description")])),
                                        html.Tbody([
                                            html.Tr([html.Td("Gender"), html.Td("The gender of the student (male/female)")]),
                                            html.Tr([html.Td("Race/ethnicity"), html.Td("The student's racial or ethnic background (Asian, African-American, Hispanic, etc.)")]),
                                            html.Tr([html.Td("Parental level of education"), html.Td("The highest level of education attained by the student's parent(s) or guardian(s)")]),
                                            html.Tr([html.Td("Lunch"), html.Td("Whether the student receives free or reduced-price lunch (yes/no)")]),
                                            html.Tr([html.Td("Test preparation course"), html.Td("Whether the student completed a test preparation course (yes/no)")]),
                                            html.Tr([html.Td("Math score"), html.Td("The student's score on a standardized mathematics test")]),
                                            html.Tr([html.Td("Reading score"), html.Td("The student's score on a standardized reading test")]),
                                            html.Tr([html.Td("Writing score"), html.Td("The student's score on a standardized writing test")]),
                                                ],
                                                className="custom-table" ), ],
                                        className="table table-bordered table-hover", ), ],
                                className="card mb-4",),  ],
                        width=6  ),  ] ),
            html.Img(src='../assets/kaggle_data.png', alt="My Image", style={'width': '80%', 'height': '50%'}),
            html.Hr(className="my-4", style={"border-top": "2px solid #ccc"}),

            html.H3("Student Demographics"),
            dcc.Graph(id="scatter_plot_data"),
            html.P("Select a student index to view individual Student Demographics."),
            html.H3("Student Information by Student Index"),
            html.Div(id="demographic-table"),
            dcc.Dropdown(
                id="student-dropdown",
                options=[{"label": student_id, "value": student_id} for student_id in demographics_df["student_id"]],
                value=demographics_df["student_id"].iloc[0],
            ),
            html.H3("Student Information Overview by Demographics"),
            dcc.Graph(id="update_score_graph", figure={}),
            
            html.P(""),
            html.Hr(className="my-4", style={"border-top": "2px solid #ccc"}),

            html.H3("Neural Network Model and Results"),

            html.Img(src='../assets/neural.png', alt="My Image", style={'width': '90%', 'height': '60%'}),
            html.Hr(className="my-4", style={"border-top": "2px solid #ccc"}),
            html.H3("Kaggle Data Set Model Accuracy"),
            html.Div(
                [
                    html.Table(
                        [
                            html.Thead(
                                html.Tr([html.Th("Test"), html.Th("Accuracy")])
                            ),
                            html.Tbody(
                                [
                                    html.Tr([html.Td("Reading"), html.Td("0.616")]),
                                    html.Tr([html.Td("Writing"), html.Td("0.672")]),
                                    html.Tr([html.Td("Math"), html.Td("0.608")]),
                                    html.Tr([html.Td("Overall (average >= 70)"), html.Td("0.640")])
                                ]
                            ),
                        ],
                        style={"margin": "10px"},

                    )
                ],
                className="col-md-5"
            ),
            html.P(""),
            html.A(
            html.Img(src='../assets/kaggle_tableau.png', alt="My Image", style={'width': '90%', 'height': '60%','padding-left': '60px'}),
                        href="https://public.tableau.com/app/profile/sahmirah.muhammad/viz/KaggleStudentPerformance/Story1",
                        target="_blank"
                    ),
                ],
        className="container mt-4",
        ),],
        fluid=True,
        )
    )
   return layout

@app1.callback(
    Output("scatter_plot_data", "figure"),
    Output("demographic-table", "children"),
    Output("update_score_graph", "figure"),
    Input("student-dropdown", "value"),
)
def update_student_data(student_index):
    scatter_data = px.scatter(
        demographics_df,
        x="math score",
        y="writing score",
        color="gender",
        template="plotly_dark",
        labels={"race_ethnicity": "Race/Ethnicity"},
    )
    student_row = demographics_df.loc[demographics_df["student_id"] == student_index]
    student_id = student_row["student_id"].iloc[0]
    gender = student_row["gender"].iloc[0]
    race_ethnicity = student_row["race_ethnicity"].iloc[0]
    parent_education = student_row["parent_education"].iloc[0]
    lunch = student_row["lunch"].iloc[0]
    test_prep = student_row["test preparation course"].iloc[0]
    math_score = student_row["math score"].iloc[0]
    reading_score = student_row["reading score"].iloc[0]
    writing_score = student_row["writing score"].iloc[0]
    demographic_table = html.Table(
        [
            html.Tr([html.Td("Student ID:"), html.Td(student_id)]),
            html.Tr([html.Td("Gender:"), html.Td(str(gender))]),
            html.Tr([html.Td("Race/Ethnicity:"), html.Td(str(race_ethnicity))]),
            html.Tr([html.Td("Parental Level of Education:"), html.Td(str(parent_education))]),
            html.Tr([html.Td("Lunch:"), html.Td(str(lunch))]),
            html.Tr([html.Td("Test Preparation Course:"), html.Td(str(test_prep))]),
            html.Tr([html.Td("Math Score:"), html.Td(str(math_score))]),
            html.Tr([html.Td("Reading Score:"), html.Td(str(reading_score))]),
            html.Tr([html.Td("Writing Score:"), html.Td(str(writing_score))]),
        ],
        style={"margin-top": "20px", "margin-bottom": "20px"},
    )
    subjects = ["Math", "Reading", "Writing"]
    scores = [math_score, reading_score, writing_score]
    score_df = pd.DataFrame({"Subject": subjects, "Score": scores})
    score_data = px.bar(
        data_frame=score_df,
        x="Subject",
        y="Score",
        labels={"Score": "Score"},
        hover_data={"Subject": False, "Score": ":.2f"},
    )
    score_data.update_traces(hovertemplate="Subject: %{x}<br>Score: %{y}", marker_color="black")
    return scatter_data, demographic_table, score_data

app1.layout = layout1

if __name__ == "__main__":
    app1.run_server(port=8051, debug=True)