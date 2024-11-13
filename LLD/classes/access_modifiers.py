class Student:
    def __init__(self, name, age, address):
        self.__name = name # private variable
        self.age = age
        self._address = address # protected variable


s1 = Student('John', 20, 'New York')
# print(s1.__name)  # will throw an error

## hack
print(s1._Student__name)

print(s1._address)

