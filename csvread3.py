import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.express as px

# data = pd.read_csv('csv/data_182small.csv', sep=';', parse_dates=['date'], dayfirst=True)
# data['rate'] = round(data['rate'], 2)
# print(unique_codes)
# df = [go.Scatter(
#     x=data['date'],
#     y=data['rate'],
#     title="setting up colour palette",
#     color_continuous_scale=["orange", "red", "green", "blue", "purple"])]
# plotly.offline.plot(df)

data = pd.read_csv('csv/data_182small.csv', encoding = 'UTF-8', sep=';', parse_dates=['date'], dayfirst=True)
data['rate'] = round(data['rate'], 2)
fig = px.scatter(data,
    color='letter_code',
    x=data['date'],
    y=data['rate'],
    title="Курс валют",
    color_continuous_scale=["orange", "red", "green", "blue", "purple"],
    template = "plotly_dark")

fig.show()
