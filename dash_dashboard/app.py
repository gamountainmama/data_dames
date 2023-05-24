from dash import dcc, html, Input, Output
from dash.dependencies import State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from pages import app1, app2, app3, app4


navbar = Navbar()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


app.validation_layout = html.Div([
    app.layout,
    app1.layout1(),
    app2.layout2(),
    app3.layout3(),
    app4.layout4(),
])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/app1':
        return app1.layout1()
    elif pathname == '/app2':
        return app2.layout2()
    elif pathname == '/app3':
        return app3.layout3()
    elif pathname == '/app4':
        return app4.layout4()
    else:
        return '404 Page not found'


if __name__ == '__main__':
    app.run_server(debug=True)
