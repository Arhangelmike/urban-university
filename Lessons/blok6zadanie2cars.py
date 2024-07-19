class Venicle:

    owner: str
    __model: str
    __engine_power: int
    __color: str
    __COLOR_VARIANTS = ['black', 'grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'light_grey', 'dark_grey',
                        'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan',
                        'white']

    def get_model(self):
        print(f'Модель: {self.__model}')


    def get_horsepower(self):
        print(f'Мощность двигателя:  {self.__engine_power}')


    def get_color(self):
        print(f'Цвет: {self.__color}')


    def print_info(self):
        print(self.owner)
        print(self.get_model)
        print(self.get_horsepower)
        print(self.get_color)



    def set_color(self, new_color):
        self.new_color = new_color
        if new_color in Venicle.__COLOR_VARIANTS:
            print(f'{new_color}')
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Venicle):
    __PASSENGERS_LIMIT = 5
    def __init__(self, *args):
        pass
        # print(*args)


#  Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# # Изначальные свойства
vehicle1.print_info()
#
# # Меняем свойства (в т.ч. вызывая методы)
# vehicle1.set_color('Pink')
# vehicle1.set_color('BLACK')
# vehicle1.owner = 'Vasyok'
#
# # Проверяем что поменялось
# vehicle1.print_info()
