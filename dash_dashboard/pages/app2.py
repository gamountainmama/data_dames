import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd
import pathlib
import plotly.express as px
from dash import dcc, html, Input, Output
from flask import Flask, url_for

'''This is the app for the Independent School in Florida.'''

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
PC_CSV_PATH = DATA_PATH.joinpath("new_PC_data.csv")
PCdemographics_df = pd.read_csv(PC_CSV_PATH)


app2 = dash.Dash(
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

@app2.callback(
    Output("scatter_plot_data2", "figure"),
    Input("student-dropdown2", "value"),
)
def update_student_data2(student_id):
    filtered_df = PCdemographics_df[PCdemographics_df["StudentID"] == student_id]
    
    # Convert numerical grades to categorical labels
    grade_labels = {
        9: "Grade 9",
        10: "Grade 10",
        11: "Grade 11",
        12: "Grade 12",
        "Unknown": "Unknown"
    }
    filtered_df.loc[:, "Grade"] = filtered_df["Grade"].map(grade_labels)
    
    scatter_data2 = px.scatter(
        filtered_df,
        x="Course_Type",
        y="Section_Grade",
        color="Grade",
        template="plotly_dark",
        labels={"Course_Type": "Course Type"},
        color_discrete_map={
            "Grade 9": "blue",
            "Grade 10": "green",
            "Grade 11": "orange",
            "Grade 12": "rgb(255, 0, 0)",  # Change the color mapping to red
            "Unknown": "gray"
        }
    )

    scatter_data2.update_traces(marker=dict(size=28,color="red"))
    scatter_data2.update_layout(title="Course Grade per Student Data")

    return scatter_data2


@app2.callback(
    Output("scatter_plot_alldata", "figure"),
    Input("student-dropdown2", "value"),
)
def update_all_student(student_id):
    scatter_all_data = px.scatter(
        PCdemographics_df,
        x="Grade",
        y="Section_Grade",
        color="Course_Type",
        template="plotly_dark",
        labels={"Course_Type": "Course Type"},
        color_discrete_map={
            "Grade 9": "blue",
            "Grade 10": "green",
            "Grade 11": "orange",
            "Grade 12": "red",
            "Unknown": "gray"
        },
    )

    scatter_all_data.update_traces(marker=dict(size=18))
    scatter_all_data.update_layout(title="Course Grades per Grade")

    return scatter_all_data

def layout2():
    print("Rendering layout2")
    layout = html.Div([
        navbar,
        dbc.Container([   
            html.Div([
                html.H1("The Problems in Standardizing Educational Data", className="display-4"),
                html.P('''Establishing standardized grading systems in independent schools can be a challenge due to the wide range of courses and resources. 
                    The numerous course offerings in independent schools also makes it difficult to easily find patterns. Furthermore, the demographics are primarily homogenic
                    making it difficult to identify demographic issues.'''),  # Added a comma at the end of this line
                html.H2("Florida Private School Data", style={"padding": "10px"}),
                html.Div([
                    html.Img(src='../assets/pc_features.png', alt="My Image", style={'width': '60%', 'height': '30%'}),
                    html.A(
                        html.Img(src='../assets/pc_tableau.png', alt="My Image", style={'width': '40%', 'height': '30%', 'padding-left': '20px'}),
                        href="https://public.tableau.com/app/profile/sahmirah.muhammad/viz/FloridaPrivateSchoolData/StudentData",
                        target="_blank"
                    )
                ]),
                html.P(''),
                dcc.Graph(id="scatter_plot_data2"),  # Add this line to display the graph
                dcc.Dropdown(
                    id="student-dropdown2",
                    options=[
                        {"label": str(student_id), "value": student_id}
                        for student_id in PCdemographics_df["StudentID"]
                    ],
                    value=PCdemographics_df["StudentID"].iloc[0],
                ),
            ]),

            dcc.Graph(id="scatter_plot_alldata"),
            html.Img(src='../assets/neural.png', alt="My Image", style={'width': '90%', 'height': '60%'}),

            
        ]),
    ])
    return layout



app2.layout = layout2

if __name__ == '__main__':
    app2.run_server(port=8052, debug=True)
