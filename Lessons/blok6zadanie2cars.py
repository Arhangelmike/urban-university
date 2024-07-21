class Venicle:
    __COLOR_VARIANTS = ['black', 'grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'light_grey', 'dark_grey',
                        'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan',
                        'white']
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color


    def get_model(self):
        # print(f'Модель: {self.__model}')
        return f'Модель: {self.__model}'


    def get_horsepower(self):
        # print(f'Мощность двигателя:  {self.__engine_power}')
        return f'Мощность двигателя: {self.__engine_power}'


    def get_color(self):
        # print(f'Цвет: {self.__color}')
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')



    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in (item.lower() for item in self.__COLOR_VARIANTS):
            #rint(f'Цвет: {new_color}')
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Venicle):
    __PASSENGERS_LIMIT = 5
    # def __init__(self, *args):
        # pass
        # print(*args)


#  Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# # Изначальные свойства
vehicle1.print_info()
#
# # Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
#
# # Проверяем что поменялось
vehicle1.print_info()
