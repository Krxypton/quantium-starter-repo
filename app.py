import pandas as pd
from dash import Dash, html, dcc

# Load the processed data
df = pd.read_csv('data/output.csv')
df = df.sort_values('date')

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Pink Morsel Sales Visualiser'),
    dcc.Graph(
        figure={
            'data': [{
                'x': df['date'],
                'y': df['sales'],
                'type': 'line'
            }],
            'layout': {
                'title': 'Pink Morsel Sales Over Time',
                'xaxis': {'title': 'Date'},
                'yaxis': {'title': 'Sales ($)'}
            }
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)