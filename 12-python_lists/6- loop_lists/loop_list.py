# thislist = ["apple", "banana", "cherry"]

#You can loop through the list items by using a for loop

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop through the index numbers
# use the range() and the len() functions to create a suitable iterable
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# You can use a while loop to print all items in a list
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#Looping Using List Comprehension
# This is the shortest syntax for looping through lists
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]










