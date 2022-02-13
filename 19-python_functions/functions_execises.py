#Exercise:
#Create a function named my_function.
def my_function():
    print("Hello from a function")

#Exercise2:
#Create a function named my_function.:
print("Hello from a function")

#Exercise3
#Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
    print(fname)

#Exercise4
#If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(kids):
    print("The youngest child is " + kids[2])

#Exercise5
#If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
    print("The younge9st child is " + kids[2])

#Exercise6
#If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname="ZULU", lname="Shaka")




