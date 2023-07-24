from dash import Dash, html, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from functions import get_stocks
from dash import dash_table

import plotly.express as px

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

def build_table (df):
    return dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

app.layout = html.Div(children=[
    html.H1(children='Stock Summary', style={'textAlign':'center'}),
    html.P(),
    dbc.Row([
        dbc.Col(html.Div('Specify timezone'), width='auto'),
        dbc.Col(dcc.Input(id='timezone-input', value= 'America/Denver'), width='auto'),
        #dbc.Col(html.A('Find timezone here: ', href='https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568'), width='auto')
]),
    html.P(),

    dbc.Row([
        dbc.Col(html.P(children='Input stock symbols', style={'textAlign':'left'}), width='auto'),
        dbc.Col(dcc.Input(id='symbol-input', value= '^DJI  AAPL  GOOG  GC=F  TSLA', style={"width": "80%"}), width=6),
    ]),
    html.P(),
    html.Button('Get Summary', id='submit-button'),
    dbc.Row(html.Div(id='datatable')),
    html.P(),

    html.Div([
    dcc.Loading(
        id="table",
        children=[html.Div([html.Div(id="loading-output")])],
        type="default",
    )
    ])
])
    

@app.callback(
    Output("loading-output", "children"),
    Input('timezone-input', 'value'),
    Input('symbol-input', 'value'),
    Input('submit-button', 'n_clicks'),
    prevent_initial_call=True
)
def update_table(timezone, symbols, n_clicks):
    symbols = list(symbols.split())
    df, local_time = get_stocks(symbols, timezone)

    return html.Div([f'The result is obtained at {local_time.strftime("%m-%d-%y %H:%M")} {timezone}', build_table(df)])


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)