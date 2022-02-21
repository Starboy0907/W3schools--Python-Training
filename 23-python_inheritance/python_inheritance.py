from unicodedata import name


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)
x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass

x = Student("James", "Dean")
x.printname()
