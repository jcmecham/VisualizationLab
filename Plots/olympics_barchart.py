from typing import Any, Union

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
from numpy.core._multiarray_umath import ndarray
from pandas import Series, DataFrame
from pandas.core.arrays import ExtensionArray

df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

n_df = df[df['Total'] > 17]

# Preparing data
data = [go.Bar(x=n_df['NOC'], y=n_df['Total'])]

# Preparing layout
layout = go.Layout(title='Rio 2016 Olympics Top 20 Medal Count', xaxis_title="Countries",
                   yaxis_title="Number of Total Medals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')