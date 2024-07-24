class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = () # (список сторон (целые числа))
        self.__color = () # (список цветов в формате RGB)
        self.filled = bool # (закрашенный, bool)

    def get_color(self):
        pass
    '''возврат три числа каждое в диапазоне от 0 до 255'''

    def __is_valid_color(self, R, G, B):
        pass

    def __is_valid_sides(self, __sides):
        pass
    '''принимает неограниченное кол-во сторон, 
    возвращает True если все стороны целые положительные числа и
     кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.'''

    def get_sides(self):
        pass # должен возвращать значениея атрибута __sides.

    def __len__(self):
        pass #  возвращать периметр фигуры.

    def  set_sides(self, *new_sides):
        pass #  принимать новые стороны, если их количество не равно sides_count,
        # то не изменять, в противном случае - менять.

class Circle(Figure):
    sides_count = 1

    def __init__(self):
        self.__radius

    def get_square(self):
        pass
    '''Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).'''


class Triangle(Figure):
    sides_count = 3
    def __init__(self):
        self.__height

    def get_square(self):
        pass
    '''Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
Метод get_square возвращает площадь треугольника.'''

class Cube(Figure):
    sides_count = 12
    def __init__(self):
        self.__sides

    def get_volume(self):
        pass
    '''Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.'''


