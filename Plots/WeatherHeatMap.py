import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Preparing data
data = [go.Heatmap(x=df['day'],
                   y=df['month'],
                   z=df['record_max_temp'],
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Average temp per week per month', xaxis_title="Day of Week",
                   yaxis_title="Month of year")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)

# labels=dict(x="Week of the month", y="Time of Day", color="Productivity"),
#                 x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday','Sunday'],
#                 y=['January', 'February', "March", "April", "May", "June", "July", "August", "September", "October",
#                    "November", "December"])


pyo.plot(fig, filename='WeatherHeatmap.html')
