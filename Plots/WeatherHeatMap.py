import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Preparing data
data = [go.Heatmap(x=df['day'],
                   y=df['month'],
                   z=df['record_max_temp'],
                   colorscale='Jet'
                   )
                   ]

# Preparing layout
layout = go.Layout(title='Record Max temp per day and month', xaxis_title="Day of Week",
                   yaxis_title="Month of year")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)




pyo.plot(fig, filename='WeatherHeatmap.html')
