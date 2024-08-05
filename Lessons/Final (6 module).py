#import os
#os.system('color')
import math

class Figure:
    side_count = 0
    __color = [255, 255, 255]
    __sides = []
    filled = False
    def get_sides (self):
        return self.__sides
    def get_color(self):
        return self.__color
    def __is_vailid_color(self, *color):
        _color = list(color)
        if isinstance(_color[0], int) and isinstance(_color[1], int) and isinstance(_color[2], int):
                if _color[0] in range(0, 256) and _color[1] in range(0, 256) and _color[2] in range(0, 256):
                    return True
                else:
                    return False
        else:
            return False
    def set_color(self, *color):
        if self.__is_vailid_color(*color) == True:
            self.__color = list(color)
    def set_new_sides(self, *side):  #  - создание списка сторон при создании НОВОГО объекта класса!
        _sides = []
        if Figure.__is_valid_sides(*side) == True:
            _sides = list(side)
            if len(_sides) == self.side_count:
                Figure.__sides = _sides
            elif self.side_count == 12 and len(side) == 1:
                _sides = []
                for j in range(self.side_count):
                    _sides.append(*side)
                Figure.__sides = _sides
            else:
                _sides = []
                for j in range(self.side_count):
                    _sides.append(1)
                Figure.__sides = _sides
            return Figure.__sides

    def set_sides(self, *side):
        _sides = []
        if Figure.__is_valid_sides(*side) == True:
            _sides = list(side)
            if len(_sides) == self.side_count:
                Figure.__sides = _sides
        return Figure.__sides

    def __is_valid_sides(*side):
        n = 0
        for j in side:
            if isinstance(j, int) and int(j) > 0:
                continue
            else:
                n += 1
        if n == 0:
            return True
        else:
            return False

    def __len__(self):
        return sum(Figure.__sides)
class Circle(Figure):
    def __init__(self, color, *side):
        self.set_color(*color)
        self.side_count = 1
        self.set_new_sides(*side)
        self.radius = round(self._Figure__sides[0]/ (6.283), 3)

    def get_square(self):
        S = round(3.1415 * self._Figure__sides[0] * self._Figure__sides[0], 3)
        return S
class Triangle(Figure):
    height = 0
    def __init__(self, color, *side):
        self.set_color(*color)
        self.side_count = 3
        self.set_new_sides(*side)
        if len(side) == 3:
            self.height = self._heigth()

    def _heigth(self):
        p = sum(self._Figure__sides)/2
        a = p * ((p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2]))
        h = 2 * math.sqrt(a)/self._Figure__sides[0]
        return round(h,3)
    def get_square(self):
        S = 1/2 * self.height * self._Figure__sides[0]
        return round(S, 3)

class Cube(Figure):
    def __init__(self, color, *side):
        self.color = color
        self.set_color(*color)
        self.side_count = 12
        self.sides = self.set_new_sides(*side)
    def get_volume(self):
        V = self.sides[0] * self.sides[0] * self.sides[0]
        return V

circle1 = Circle((255, 45, 56),5)
print(f'----Текущие параметры окружности: цвет RGB: {circle1.get_color()}, длина сторон: {circle1.get_sides()}----')
print(f'Площадь круга равна: {circle1.get_square()}')
print(f'Радиус круга равен: {circle1.radius}')
print(f'Периметр круга составляет: {len(circle1)}')

color1 = (10, 50, 200)
side1 = 25
side2 = 30
print(f'--Попробуем изменить параметры окружности: цвет на: {color1}, стороны на: {side1, side2}--!!!')
circle1.set_color(color1)
circle1.set_sides(side1, side2)
print(f'---Текущие параметры окружности будут: цвет RGB: {circle1.get_color()}, длина сторон: {circle1.get_sides()}---')
print('')


triangle1 = Triangle((10, 15, 200), 20, 18, 10)
print(f'--Текущие параметры треугольника: цвет RGB: {triangle1.get_color()}, длина сторон: {triangle1.get_sides()} --')
print(f'Периметр треугольника составляет: {len(triangle1)}')
print(f'Высота заданного треугольника составляет: {triangle1.height}')
print(f'Площадь заданного треугольника составляет: {triangle1.get_square()}')

color2 = (15, 15, 15)
side1 = 17
side2 = 22
side3 = 11
print(f'--Попробуем изменить параметры треугольника: цвет на: {color2}, стороны на: {side1, side2} --!!!')
triangle1.set_color(15, 15, 15)
triangle1.set_sides(side1, side2)
print(f'---Текущие параметры треугольника будут: цвет: {triangle1.get_color()}, стороны: {triangle1.get_sides()} ---')
print('')

cube1 = Cube((23, 45, 255), 6)
print(f'Текущие параметры куба: цвет RGB: {cube1.get_color()}, длина сторон: {cube1.get_sides()}')
print(f'Объем заданного Куба составляет: {cube1.get_volume()}')

print(f'--Попробуем изменить параметры куба: цвет на: {color1}, стороны на: {side1, side2, side3} --!!!')
cube1.set_color(color1)
cube1.set_sides(side1, side2, side3)
print(f'Текущие параметры куба будут: цвет RGB: {cube1.get_color()}, длина сторон: {cube1.get_sides()}')

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
