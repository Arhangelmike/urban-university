import pandas as pd
import plotly.graph_objects as go


data = pd.read_csv('csv/data_182small.csv', encoding='UTF-8', sep=';', parse_dates=['date'], dayfirst=True)
data['rate'] = round(data['rate'], 2)
dfA = pd.DataFrame({
    "Price": data['rate'],
    "Years": data['date'],
    "Currency": data['letter_code']
})

currencies = dfA['Currency'].unique()

fig = go.Figure()
for idx, currency in enumerate(currencies):
    filtered_data = dfA[dfA['Currency'] == currency]
    fig.add_trace(
        go.Scatter(x=filtered_data["Years"], y=filtered_data["Price"], name=currency),
    )

fig.update_layout(
    # height=400 * n_rows,
    title="Мультиграфики по валютам",
    showlegend=True  # Скрыть легенду, если она не нужна
)
fig.show()
