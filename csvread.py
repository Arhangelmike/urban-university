#   date;currency;digital_code;letter_code;rate
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('csv/1111.csv', sep=';', parse_dates=['date'], dayfirst=True)
df['rate'] = round(df['rate'], 2)
df['date'] = pd.to_datetime(df['date'])
uniq_code = df['letter_code'].unique()

fig, ax = plt.subplots()
global x, y
for u in df['date']:
    for d in df['date'].unique():

        if d == u:
            for next_code in df['letter_code'].unique():
                if (u == d):
                    y = df['rate']
                    x = df['date']

            plt.plot(x, y, label=next_code)
        else:
            continue

ax.grid()
ax.legend()
plt.show()
