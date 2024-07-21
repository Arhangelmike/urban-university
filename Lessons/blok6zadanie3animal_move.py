class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self):
        pass

    def run(self, dx):
        self.x_distance = self.x_distance + dx

#  y_distance на dy.
class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self):
        pass


    def fly(self, dy):
        self.y_distance = self.y_distance + dy




class Pegasus:
    pass

    def move(self, dx, dy):
        pass

    def get_pos(self):
        pass

    def voice(self):
        pass

p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
