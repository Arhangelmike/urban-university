import random
class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = () # (список сторон (целые числа))
        self.__color = () # (список цветов в формате RGB)
        self.filled = bool # (закрашенный, bool)

    def get_color(self):
        self.R = random.randint(0, 255)
        self.G = random.randint(0, 255)
        self.B = random.randint(0, 255)
    '''возврат три числа каждое в диапазоне от 0 до 255'''

    def __is_valid_color(self, R, G, B):
        if all(0 <= value <= 255 for value in (R, G, B)):
            print("Все значения R, G и B находятся в диапазоне от 0 до 255")
        else:
            print("Одно или несколько значений R, G или B находятся вне диапазона")

    def __is_valid_sides(self, *args):
        args_list = list(args)
        is_valid = all(i > 0 and isinstance(i, int) for i in args_list) and len(args_list) == self.sides_count
        return is_valid

    '''принимает неограниченное кол-во сторон, 
    возвращает True если все стороны целые положительные числа и
     кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.'''

    def get_sides(self):
       return self.__sides # должен возвращать значениея атрибута __sides.

    def __len__(self):
        def __len__(self):
            return sum(self.__sides) #  возвращать периметр фигуры.

    def  set_sides(self, *new_sides):
        self.__is_valid_sides(*new_sides)
        #side_list = list(new_sides)
         #  принимать новые стороны, если их количество не равно sides_count,
              # то не изменять, в противном случае - менять.
        '''Там фишка в том, что если ты передаешь список, у которого длина совпадает с sides_count, то числа из списка это и есть длины сторон 

Например: 
Triangle((200, 200, 100), 10, 6, 7)
10, 6, 7 — стороны треугольника

Circle((200, 200, 100), 6)
6 — длина окружности

Если же передается список, длина которого равна 1 (то есть просто одно число), то все стороны у фигуры будут такой длины

Например:
Triangle((200, 200, 100), 10)
10, 10, 10 — стороны треугольника
 
Cube((200, 200, 100), 9)
9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 — стороны куба

И третий вариант, когда передается список любой другой длины (кроме одного числа и sides_count), то все стороны у фигуры будут длины 1

Например:
Triangle((200, 200, 100), 10, 6)
1, 1, 1 — стороны треугольника

Triangle((200, 200, 100), 10, 6, 8, 11)
1, 1, 1 — стороны треугольника 

Circle((200, 200, 100), 10, 15, 6)
1 — длина окружности 

Cube((200, 200, 100), 9, 10, 6, 5)
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 — стороны куба'''

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


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())