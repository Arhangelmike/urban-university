import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv('csv/data_182small.csv', encoding='UTF-8', sep=';', parse_dates=['date'], dayfirst=True)
data['rate'] = round(data['rate'], 2)
dfA = pd.DataFrame({
    "Price": data['rate'],
    "Years": data['date'],
    "Currency": data['letter_code']
})

currencies = dfA['Currency'].unique()

# n_cols = 2
# n_rows = -(-len(currencies) // n_cols)  # Округление вверх
# fig = make_subplots(rows=n_rows, cols=n_cols, subplot_titles=currencies)
fig = go.Figure()
for idx, currency in enumerate(currencies):
    # row = idx // n_cols + 1
    # col = idx % n_cols + 1

    filtered_data = dfA[dfA['Currency'] == currency]
    fig.add_trace(
        go.Scatter(x=filtered_data["Years"], y=filtered_data["Price"], name=currency),
        # row=row,
        # col=col
    )

fig.update_layout(
    # height=400 * n_rows,
    title="Мультиграфики по валютам",
    showlegend=False  # Скрыть легенду, если она не нужна
)
fig.show()
# x=data['date']
# y=data['rate']
# количество данных по валюте в процентах от частоты упоминания ее в файле
# fig = px.pie(data, values=data['rate'], names=data['letter_code'], title='Data value')
# fig = px.scatter(x, y)
# fig.show()

