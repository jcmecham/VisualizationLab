import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/WEather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])
data = [go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='max_temp')]
layout = go.Layout(title='Max Temperatures from July 2014 to June 2015',
                   xaxis_title="Date", yaxis_title="Temperatures")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')