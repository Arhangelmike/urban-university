import pandas as pd
import plotly
import plotly.graph_objs as go


data = pd.read_csv('csv/data_182small.csv', sep=';', parse_dates=['date'], dayfirst=True)
data['rate'] = round(data['rate'], 2)
# print(unique_codes)
df = [go.Scatter(
    x=data['date'],
    y=data['rate'])]
plotly.offline.plot(df)


