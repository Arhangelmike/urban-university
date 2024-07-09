class Animal:
    alive = True
    fed = False
    name = ''


class Predator(Animal):
    def __init__(self, name):
        self.name = name
        Animal.__init__(self)

    def eat(self, food):
        if food.edible is True:
            self.fed = True
            self.alive = True
            print(f'{self.name}  съел {food.name}')
        else:
            self.fed = False
            self.alive = False
            print(f'{self.name}  не стал есть {food.name} ')


class Mammal(Animal):

    def __init__(self, name):
        self.name = name
        Animal.__init__(self)

    def eat(self, food):
        if Plant.edible is not True:
            self.fed = True
            self.alive = True
            print(f'{self.name}  съел {food.name}')
        else:
            self.fed = False
            self.alive = False
            print(f'{self.name}  не стал есть   {food.name}')


class Plant:
    name = ''
    edible = False


class Flower(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = False  #
        Plant.__init__(self)


class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True
        Plant.__init__(self)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
