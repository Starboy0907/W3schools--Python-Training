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
    pass                    # the child inherits the parents init function

x = Student("James", "Dean") 
x.printname()

class Pupil(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname,lname)
    def printname(self):
        print(self.firstname, self.lastname)
x = Student("Mike", "Olsen")
x.printname()

class Grasshopper(Person):
    def __init__(self, fname, lname):
        super().__init__(fname,lname)
        self.graduationyear = 2019      # Adds a property to the class

y=Grasshopper("Sizzla","Zou")
y.printname()

class Apprentice(Person):
    def __init__(self,lname, fname, year):  #adds the parameter
        super().__init__(lname, fname, year)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

z = Student ("Gary", "Mcmaley")
z.printname()






