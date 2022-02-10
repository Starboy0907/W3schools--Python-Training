# List Comprehension is the shorest syntax for creating a list based on the values of an existing list

# without list comprehension:
fruits = ["apple", "banana", "cherry"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# with list comprehension, you can do all that with one line of code!
fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# list comprehension syntax: newlist = [expression for item in iterable if condition == True]
# Example 2
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# The condition is optional; Example 3
newlist = [x for x in fruits]
print(newlist)

# The iterable can be any iterable object, like a list, tuple, dictionary, or set
# You can use the range() function to create an iterable
newlist = [x for x in range(10)]
print(newlist)

# Same example with a condition
newlist = [x for x in range(10) if x < 5 ]
print(newlist)

# Expression- The expression is the current item in iteration, but is also the outcome, which you can manipulate before it becomes a list item in the new list
newlist = [x.upper() for x in fruits]
print(newlist)

# You can set the outcome to whatever you like
newlist = ['hello' for x in fruits]
print(newlist)

# Return "orange" instaed of "banana"
newlist = [x if x != "banana" else "orange" for x in fruits]



