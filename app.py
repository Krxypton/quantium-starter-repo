import pandas as pd
from dash import Dash, html, dcc, Input, Output

# Load the processed data
df = pd.read_csv('data/output.csv')
df = df.sort_values('date')

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Pink Morsel Sales Visualiser', style={
        'textAlign': 'center',
        'color': '#ff6b6b',
        'fontFamily': 'Arial, sans-serif',
        'marginBottom': '10px'
    }),

    html.Div([
        html.Label('Filter by Region:', style={'fontFamily': 'Arial', 'fontWeight': 'bold'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',
            inline=True,
            style={'fontFamily': 'Arial', 'margin': '10px 0'}
        )
    ], style={'textAlign': 'center'}),

    dcc.Graph(id='sales-chart')

], style={
    'maxWidth': '1000px',
    'margin': '0 auto',
    'padding': '20px',
    'backgroundColor': '#f9f9f9',
    'borderRadius': '10px'
})

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(region):
    if region == 'all':
        filtered = df
    else:
        filtered = df[df['region'] == region]

    return {
        'data': [{
            'x': filtered['date'],
            'y': filtered['sales'],
            'type': 'line',
            'line': {'color': '#ff6b6b'}
        }],
        'layout': {
            'title': f'Pink Morsel Sales Over Time ({region.capitalize()})',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Sales ($)'},
            'plot_bgcolor': '#f9f9f9',
            'paper_bgcolor': '#f9f9f9'
        }
    }

if __name__ == '__main__':
    app.run(debug=True)