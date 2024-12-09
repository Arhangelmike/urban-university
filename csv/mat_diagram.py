import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_182small.csv', sep=';', parse_dates=['date'], dayfirst=True)

fig, ax = plt.subplots(figsize=(8,8))

# df['letter_code'].value_counts().plot.pie()
explode_val = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# берем уникальные названия
y = df['letter_code'].unique()
x = round(df.groupby('letter_code')['rate'].sum(), 2)
data_sorted = x.sort_values(ascending=False)
top_10 = data_sorted[:10]
plt.pie(top_10, labels=top_10.index, autopct='%2.2f%%', shadow = True, explode = explode_val)


plt.ylabel('Доли сумм объемов купленных  Топ 10')
plt.title('Графики валют')
plt.grid()
plt.legend(top_10, labels=top_10, loc="upper right")
plt.show()
