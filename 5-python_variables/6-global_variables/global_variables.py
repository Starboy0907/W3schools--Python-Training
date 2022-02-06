# Global variables can be used inside and outside a function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# Create a variable inside a function as the global variable with the global keyword and you can also change a global variable with the global keyword

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()

print("Python is " + x)

# To create a global variable inside a function, you can use the global keyword
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)