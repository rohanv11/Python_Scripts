import copy

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

p1 = Person('John', 20, 'New York')
p2 = copy.copy(p1)
p3 = copy.deepcopy(p1)