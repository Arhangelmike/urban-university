import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('csv/data_182small.csv', sep=';', parse_dates=['date'], dayfirst=True)
unique_codes = data['letter_code'].unique()
data['rate'] = round(data['rate'], 2)
sns.lineplot(
    x="date",
    y="rate",
    hue='letter_code',
    legend = 'brief',
    data=data)

plt.show()
