class Buiding:
    value = 0
    def __init__(self):
        Buiding.value += 1
        print(f'Создан {Buiding.value} -й экземпляр класса')

i=1
while i <=40:
    i += 1
    h1 = Buiding()
