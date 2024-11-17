import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('csv/data_182small.csv', sep=';', parse_dates=['date'], dayfirst=True)
df['rate'] = round(df['rate'], 2)
df['date'] = pd.to_datetime(df['date'])

unique_codes = df['letter_code'].unique()
plt.figure(figsize=(20, 12))

for code in unique_codes:
    currency_data = df[df['letter_code'] == code]
    plt.plot(currency_data['date'], currency_data['rate'], label=code)


plt.xlabel('Дата')
plt.ylabel('Курс')
plt.title('Графики курсов валют')
plt.grid()

plt.show()
