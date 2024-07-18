class Venicle:
    owner=''
    __model=''
    __engine_power=0
    __color=''
    __COLOR_VARIANTS = ['black', 'grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'light_grey', 'dark_grey',
                        'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan',
                        'white']

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
        if new_color in Venicle.__COLOR_VARIANTS:
            print(f'{new_color}')
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Venicle):
        __PASSENGERS_LIMIT = 5



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
