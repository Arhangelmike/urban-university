#   date;currency;digital_code;letter_code;rate
import csv
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('csv/data_182.csv', sep=';', parse_dates=['date'], dayfirst=True)
df['rate'] = round(df['rate'], 2)
df = df.sort_values(by='date', ascending=True)
unique_codes = df['letter_code'].unique()

plt.figure(figsize=(15, 15))
for code in unique_codes[14:15]:
        currency_data = df[df['letter_code'] == code]
        plt.plot(currency_data['date'], currency_data['rate'], label=code)

plt.xlabel('Дата')
plt.ylabel('Курс')
plt.title('Графики курсов валют')
plt.grid()

plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45, ha='right')

y_ticks = range(int(df['rate'].min()), int(df['rate'].max()) + 1000, 1000)
plt.yticks(y_ticks)

plt.legend(title='Валюта', bbox_to_anchor=(1.1, 1), loc='upper left', borderaxespad=0.)
plt.tight_layout()

plt.show()
