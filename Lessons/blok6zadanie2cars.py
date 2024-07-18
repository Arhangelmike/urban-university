class Venicle:
    owner=''
    __model=''
    __engine_power=0
    __color=''
    __COLOR_VARIANTS = ['black', 'grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'light_grey', 'dark_grey',
                        'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan',
                        'white']
'''Атрибут owner(str) - владелец транспорта. (владелец может меняться)
   Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
   Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
   Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
         А так же атрибут класса:
   Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)'''

class Sedan(Venicle):
    def __init__(self):
        __PASSENGERS_LIMIT = 5

'''Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
Метод print_info - распечатывает результаты методов (в том же порядке): 
                   get_model, get_horsepower, 
                   get_color; а так же владельца в конце в формате "Владелец: <имя>"
Метод set_color - принимает аргумент new_color(str),
                  меняет цвет __color на new_color, 
                  если он есть в списке __COLOR_VARIANTS, 
                  в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".'''

    def get_model(self):
        print(f'Модель: {Venicle.__model}')


    def get_horsepower(self):
        print(f'Мощность двигателя:  {Venicle.__engine_power}')


    def get_color(self):
        print(f'Цвет: {Venicle.__color}')

    def print_info(self):
        print(f'  {self.get_model}, {self.get_horsepower}, {self.get_color} ,  {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        is new_color in __COLOR_VARIANTS:
            print(f'{new_color}')
        else
            print(f'Нельзя сменить цвет на {new_color}')



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
