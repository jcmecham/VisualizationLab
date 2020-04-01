import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

n_df = df[df['Total'] > 17]

trace1 = go.Bar(x=n_df['NOC'], y=n_df['Gold'], name='Gold',
                marker={'color': '#CD7F32'})
trace2 = go.Bar(x=n_df['NOC'], y=n_df['Silver'], name='Silver',
                marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=n_df['NOC'], y=n_df['Bronze'], name='Bronze',
                marker={'color': '#FFD700'})
layout = go.Layout(title='Rio Olympics 2016 Top 20 Countries Medals Won',
                   xaxis_title="Country", yaxis_title="Medals Won",
                   barmode='stack')
data = [trace1, trace2, trace3]
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')