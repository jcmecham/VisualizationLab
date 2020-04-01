import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])
trace1 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Max Temp')
trace2 = go.Scatter(x=df['date'], y=df['actual_min_temp'], mode='lines', name='Min Temp')
trace3 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='Mean Temp')
data = [trace1, trace2, trace3]
layout = go.Layout(title='Max, Min and Mean Temps for each month from July 2014 - June 2015',
                   xaxis_title="Date", yaxis_title="Temperatures")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')