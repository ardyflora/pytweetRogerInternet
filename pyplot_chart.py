import plotly 
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

import pandas as pd

plotly.tools.set_credentials_file(username='eripflo', api_key='qdHQ7u7VwoR5a4byVyuA')

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

trace_high = go.Scatter(
                x=df.Date,
                y=df['AAPL.High'],
                name = "AAPL High",
                line = dict(color = '#17BECF'),
                opacity = 0.8)

trace_low = go.Scatter(
                x=df.Date,
                y=df['AAPL.Low'],
                name = "AAPL Low",
                line = dict(color = '#7F7F7F'),
                opacity = 0.8)

data = [trace_high,trace_low]

fig = dict(data=data, layout=layout)
py.iplot(fig, filename = "Manually Set Range")
py.image.save_as({'data':data}, 'scatter_plot', format='png')