from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_excel("Pasta1.xlsx")

servidores=['Catia', 'Autocad', 'RH', 'TI', 'Cognix']

fig = go.Figure(data=[
    go.Bar(name='Livre', x=servidores, y=[500, 200, 100, 50, 50]),
    go.Bar(name='Usado', x=servidores, y=[500, 800, 900, 950, 950])
])

# Change the bar mode
fig.update_layout(barmode='stack')
app.layout = html.Div(children=[
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
fig.update_layout(title_text='Servidores Isringhausen')

fig.show()



if __name__ == '__main__':
    app.run(debug=True)
