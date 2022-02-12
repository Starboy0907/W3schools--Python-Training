#1 This will raise an exception, because x is not defined
try: # the try block lets you test a block of code for errors.
    print(x) 
except:   ## The except block lets you handle the error
    print("An exception occured")

print(x)

# Many Exceptions
#2 You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#3 Finally- this block, if specified, will be executed regardless if the try block raises and error or not

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

#4 The try block will raise an error when trying to write to a read-only file:

try:
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrong when")
    finally:
        f.close()
except:
    print("Something went wrong when writing to the file")


# Raise an exception
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
    
    





