import pandas as pd
import random
import matplotlib.pyplot as plt
# читаем набор данных
df = pd.read_csv('csv/data_182small.csv', sep=';', parse_dates=['date'], dayfirst=True)
# Готовим данные, округляем до второго знака полсе запятой и переводим формат даты в человекочитаемый вид
df['rate'] = round(df['rate'], 2)
df['date'] = pd.to_datetime(df['date'])
# готовим лист всех валют, можно и через df['letter_code'].unique()
letter = ['AUD', 'BGN', 'HUF', 'DKK', 'USD', 'INR', 'CAD', 'CNY', 'NOK', 'PLN', 'SGD',
          'TRY', 'FRF', 'GBP', 'SEK', 'CHF', 'JPY', 'XDR', 'DEM', 'ATS', 'BEF', 'GRD', 'IEP',
          'ISK', 'ESP', 'ITL', 'NLG', 'PTE', 'TRL', 'FIM', 'XEU', 'EEK', 'LVL', 'LTL', 'KZT',
          'KGS', 'MDL', 'BYB', 'CZK', 'UZS', 'AZM', 'AMD']
# выбор 10-ти случайных валют из списка, для улучшения читаемости графика
currency_list = random.sample(letter, 10)
# делаем выборку из всего набора данных строк содержащих эти валюты
filtered_df = df[df['letter_code'].isin(currency_list)]
# из отсортированных данных выбираем два столбца дата и курс для построения графика
x = filtered_df[filtered_df['letter_code'].isin(currency_list)]['date']
y = filtered_df[filtered_df['letter_code'].isin(currency_list)]['rate']
# создаем список цветов для окрашивания графиков разных валюют разными цветами
colors=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
       for j in range(10)]
#создаем словарь цветов для передачи на отрисовку
color_dic = dict(zip(currency_list, colors))


# формируем варианты для того чтобы не запускать программу каждый раз когда надо показать
# как выглядит видоизмененный график
while True:
    choise = int(input(
        f'Приветствую!. Выберите график: \n1 - график с цветом.\n2 - график без цвета\n3 - график без цвета полный\n'))
    if choise == 1:
        # -------- цветной для 10 курсов валют
        '''	это метод создания графика, объединяющий инициализацию области для рисунка (fig) и осей (ax),
			на которых впоследствии будут отображаться данные.'''
        fig, ax = plt.subplots(figsize=(15, 8))
        '''строим график, который соединит точки и окрасит указаным набором цветов для каждой валюты'''
        plt.scatter(x, y, marker=".", s=1, c=filtered_df['letter_code'].map(color_dic))
        # подпишем ось Х
        plt.xlabel('Дата')
        # подпишем ось У
        plt.ylabel('Курс')
        # подпишем название графика
        plt.title('Графики курсов валют')
        plt.grid()
        plt.show()
        # --------
        continue
    if choise == 2:
        # -------- вывод для примера как выглядит график если его не окрашивать
        fig, ax = plt.subplots(figsize=(15, 8))
        plt.scatter(x, y, marker=".", s=1)
        plt.xlabel('Дата')
        plt.ylabel('Курс')
        plt.title('Графики курсов валют 10 без цвета')
        plt.grid()
        plt.show()
        # --------
        continue

    if choise == 3:
        # --------вывод графика для примера насколько не читаемый график если не сортировать его
        #
        fig, ax = plt.subplots(figsize=(15, 8))
        plt.scatter(df['date'], df['rate'], marker=".", s=1)
        plt.xlabel('Дата')
        plt.ylabel('Курс')
        plt.title('Графики курсов валют все без цвета')
        plt.grid()
        plt.show()
        # --------
        continue
