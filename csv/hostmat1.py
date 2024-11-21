import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# берём исходные данные из файла
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

# указываем данные, с которыми будем работать
x_var = 'manufacturer'
groupby_var = 'class'
# готовим данные
df_agg = df.loc[:, [x_var, groupby_var]].groupby(groupby_var)
vals = [df[x_var].values.tolist() for i, df in df_agg]

# формируем цвета и категории
colors = [plt.cm.Spectral(i/float(len(vals)-1)) for i in range(len(vals))]
n, bins, patches = plt.hist(vals, df[x_var].unique().__len__(), stacked=True, density=False, color=colors[:len(vals)])

# добавляем легенду
plt.legend({group:col for group, col in zip(np.unique(df[groupby_var]).tolist(), colors[:len(vals)])})
# и общую надпись
plt.title(f"Гистограмма с категориями по классам машин для разных производителей", fontsize=22)
# подписываем оси
plt.xlabel('Производитель')
plt.ylabel("Частота")
plt.ylim(0, 40)
# выводим график
plt.show()