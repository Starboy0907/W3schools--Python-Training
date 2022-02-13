#Python Function
# Creating  a Function
def my_function():
    print('Hello from a function')

# Calling a Function
def my_function():
    print("Hello froma function")
my_function()

# Arguments
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Parameters or Arguments?
# Number of Arguments
# The function expects two argument and expects two arguments

#1 Function with 2 arguments

def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")

#2 The function expect two arguments, but gets only 1:

def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil")

#3 Arbitrary Arguments, *args # takes any number of arguments to form a list

def my_function(*kids): 
    print("The youngest child is " + kids[2])
my_function("Emil","Tobias", "Linus")

#4 Keyword Arguments

def my_function(child3, child2, child1): 
    print("The youngest child is" + child3)
my_function(child1 = "Emil", child2= "Tobias", child3 = "Linus") #keywords are set equal to values to form key, value pairs

#5 Arbitrary Keyword Argument, **kwargs 

def my_function(**kid): # **kwargs take in any number of key, value arguments to form dictionary
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes" ) 

#6 Default Parameter Values

def my_function(country = "Norway"): # you can create a default value by setting a variable equal to a value in the function declaration
    print("I am from" + country)

my_function("Sweden")
my_function("India")
my_function() # the default value will be used in this function
my_function("Brazil")

#7 Passing a list in as an argument
def my_function(food): # food is the parameter
    for x  in food: #the food parameter is a list 
        print(x) 
fruits = ['apple','banana','cherry']
my_function(fruits) #fruits is the argument and is a list


#8 Return Values
# To let a function return a value, use the return statement
def function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#9 The pass Statement
# Function definitions cannot be empty but if, for some reason you have a function withot content put in the pass statement to avoid an error
def myfunction():
    pass

#10 Recursion
# recursion happen when a function calls itself
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        return  0
    return result
print("\n\nRecursion Example Results")
tri_recursion(7)




















 