import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
df = df.apply(lambda x : x.str.strip() if x.dtype == "object" else  x)

new_df = df.groupby(['month']).agg(
    { 'actual_max_temp': 'mean', 'actual_min_temp': 'mean'}).reset_index()
data = [
    go.Scatter(x=new_df['actual_max_temp'],
               y=new_df['actual_min_temp'],
               mode='markers',
               marker=dict(size=30, color=10, showscale=True),
               text=new_df["month"]
               )
]
layout = go.Layout(title='Max and Min temp per Month', xaxis_title="Max temp",
                   yaxis_title="Min temp", hovermode='closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='WeatherBubblechart.html')