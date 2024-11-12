#   date;currency;digital_code;letter_code;rate
import csv
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('csv/data_182small.csv', sep=';', parse_dates=['date'], dayfirst=True)
unique_codes = data['letter_code'].unique()
data['rate'] = round(data['rate'], 2)
# print(unique_codes)
sns.lineplot(
    x="date",
    y="rate",
    hue='letter_code',
    legend = 'auto',
    data=data)

plt.show()
