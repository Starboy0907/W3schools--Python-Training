# A class is an object constructor

#Create a class
class MyClass:
  x = 5
  print(x) # Added this print statement to make the class print something
print(MyClass) #Will show that MyClass is a class object
p1 = MyClass #creates an instance of a class
print(p1.x) #prints a class attribute with dot notation
#You can use the class to create objects

# The __init__ functions always executed when the class is being initiated
# The __init__ function is used to assign values, or other operations that need to be done upon instantiation.

#Assigning attributes name and age to the person class

class Person:
    def __init__(self, name, age): #The __init__ function is a function complete with the def keyword and parameters
      self.name = name # The parameters are variables that need to be initailized in the init function
      self.age = age

    def myfunc(self): #This is a class method and self is passed in to reference the current instance of the class...
      print("Hello my name is " + self.name) #...and to access the variables of the class.

p1 = Person("John", 36) #creates an instance of the class when the necessary arguments are passed in

print(p1.name) #prints an attribute of the object with the dot notation

print(p1.age)

p1.myfunc() #The object or instance can access the class methods with the dot notation.

p1.age = 40 # You access variables with the dot notation

print(p1.age)

#You can delete the properties of object with the delete keyword.
#del p1.age
print(p1.age)

#Output:
# Traceback (most recent call last):
#   File "demo_class7.py", line 13, in <module>
#     print(p1.age)
# AttributeError: 'Person' object has no attribute 'age'

#You can delete objects with the delete keyword:
# del p1
print(p1)

#  Traceback (most recent call last):
#   File "demo_class8.py", line 13, in <module>
#     print(p1)
# NameError: 'p1' is not defined

#The pass statement--- acts like a placeholder for the code of a function so as not trigger errors while the function is in development.
class Person:
    pass










