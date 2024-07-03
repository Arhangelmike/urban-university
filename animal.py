class animal:
    alive = True
    fed = False
    name = ''


class predator(animal):
    def __init__(self, name):
        self.name = name


    def eat(self, food):
        self.food = food
        if food == True:
            animal.fed = True
            print(f'{self.name}  съел {food.name}')
        else:
            animal.alive = False
            print(f'{self.name}  не стал есть {food.name}')




class mammal(animal):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food
        if food == True:
            animal.fed = True
            print(f'{self.name}  съел  {food.name}')
        else:
            animal.alive = False
            print(f'{self.name} не стал есть  {food.name}')


class plant:
    edible = False
    name = ''


class flower(plant):
    def __init__(self, name):
        self.name = name



class fruit(plant):
    def __init__(self, name):
        self.name = name
        plant.edible = True


a1 = predator('Волк с Уолл-Стрит')
a2 = mammal('Хатико')
p1 = flower('Цветик семицветик')
p2 = fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)