import pandas as pd
import matplotlib.pyplot as plt
# читаем файл
df = pd.read_csv('data_182small.csv', sep=';', parse_dates=['date'], dayfirst=True)
# готовим данные округляем, убираем данные с пропуском параметров, меняем отражаемый формат времени
df['rate'] = round(df['rate'], 2)
df['date'] = pd.to_datetime(df['date'])
df = df.dropna()
#  создаем список уникальных имен валют
unique_codes = df['letter_code'].unique()


# формируем подложку графика
fig, ax = plt.subplots(figsize=(15,8))
# для каждой валюты создаем график
for code in unique_codes:
    currency_data = df[df['letter_code'] == code]
    plt.plot(currency_data['date'], currency_data['rate'], label=code)

#  подписываем оси и график
plt.xlabel('Дата')
plt.ylabel('Курс')
plt.title('Графики курсов валют')
plt.grid()
# отобразить график
plt.show()
