class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if food.edible:
            self.fed = True
            #self.alive = True
            print(f'{self.name}  съел {food.name}')
        else:
            self.fed = False
            self.alive = False
            print(f'{self.name}  не стал есть {food.name} ')



class Predator(Animal):
    def __init__(self, name):
        self.name = name




class Mammal(Animal):
    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name



class Flower(Plant):
    def __init__(self, name):
        self.name = name



class Fruit(Plant):
    edible = True

    def __init__(self, name):
        self.name = name

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
