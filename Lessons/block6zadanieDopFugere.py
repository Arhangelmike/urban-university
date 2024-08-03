import  math
class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__color = list(color)
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled = False


    def get_color(self):
        return self.__color


    def __is_valid_color(self, R, G, B):
        return all(isinstance(colors1, int) and 0 <= colors1 <= 255 for colors1 in (R, G, B))


    def set_color(self, R, G, B):
        if self.__is_valid_color(R, G, B):
            self.__color = (R, G, B)


    def get_sides(self):
        return self.__sides


    def __is_valid_sides(self, *args):
        return all(isinstance(args1, int) and args1 > 0 for args1 in args)


    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


    def __len__(self):
        return sum(self.__sides) #  возвращать периметр фигуры.

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        #self.__radius = self._Figure__sides[0]

    def get_square(self):
        Pi = math.pi
        self.__radius = self.__sides/(2*Pi)
        R = self.__radius
        return Pi * R * R


class Triangle(Figure):
    sides_count = 3
    def __init__(self):
        self.__height

    def get_square(self, a, b, c):
        p = (a+b+c)/2
        h = 2*math.sqrt((p*(p-a)*(p-b)*(p-c))/a)
        s = (a*h)/2
        return s
    '''Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
Метод get_square возвращает площадь треугольника.'''

class Cube(Figure):
    sides_count = 12


    def __init__(self, color, *sides):
        side = sides[0] if len(sides) == 1 else 1
        super().__init__(color, *[side] * self.sides_count)

    def get_volume(self):
        return self.get_sides()[0] ** 3



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