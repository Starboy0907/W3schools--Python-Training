# Boolean Values
# You can evaluate any expression in python and get one of two values
print(10>9)
print(10==10)
print(10<9)

#You can print a statement based on whether a statement is true or false:
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# The bool() function allows you to evaluate any value, and give you true or false in return
print(bool("Hello"))
print(bool(15))

# Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Most values are true except empty ones
# The following will return true:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some values are false
# The following will return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# An object made from a class with a __len__ function that returns false or 0 will also evaluate to FALSE
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

# You can return function that return a boolean value
def myFunction():
    return True
print(myFunction())

# You can execute code based on the boolean answer of a function:
# Print yes if the boolean return True, otherwise print "No!"

def myFunction():
    return True
if myFunction:
    print("Yes")
else:
    print("No")

# You can use the isinstance() function to determine if an object is of a certain data type
x = 200
print(isinstance(x,int))







