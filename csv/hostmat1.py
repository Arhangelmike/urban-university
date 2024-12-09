import pandas as pd
import matplotlib.pyplot as plt
# Готовим данные, округляем до второго знака полсе запятой и переводим формат даты в человекочитаемый вид,убираем неполные данные
df = pd.read_csv('data_182small.csv', sep=';', parse_dates=['date'], dayfirst=True)
df['rate'] = round(df['rate'], 2)
df['date'] = pd.to_datetime(df['date'])
df = df.dropna()
#
fig, ax = plt.subplots(figsize=(15,8))
#  отбираем данные для построения курсов
x = df[df['letter_code'] == 'GBP']['date']
y = df[df['letter_code'] == 'GBP']['rate']
x2 = df[df['letter_code'] == 'CHF']['date']
y2 = df[df['letter_code'] == 'CHF']['rate']
x3 = df[df['letter_code'] == 'SEK']['date']
y3 = df[df['letter_code'] == 'SEK']['rate']
# формируем график
plt.bar(x, y, color ='g')
plt.bar(x2, y2, color ='y')
plt.bar(x3, y3, color ='b')
#  подписываем оси
plt.xlabel('Дата')
plt.ylabel('Курс')
plt.title('Графики курсов валют')
plt.grid()
#  рисуем график
plt.show()