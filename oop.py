class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

class Student(Person):
    def __init__(self, fname, age):
        Person.__init__(self, fname, age)
    def printname(self):
        print(self.name, self.age)

p1 = Person("John", 36)
print(p1.name, p1.age)
x = Student("Mike", 41)
x.printname()