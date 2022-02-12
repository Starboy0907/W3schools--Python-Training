# Python For Loop
#1 basic for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#2 Looping through a string
for x in "banana":
    print(x)

#3 The break statement
# you can stop the loop before it is set to stop
fruits = ["apple", "banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#4 
fruits = ['apple', 'banana', 'cherry'] 
for x in fruits:
    if x == "banana":
        break
    print(x)

#5 The continue statement
fruits = ['apple', 'banana', 'cherry'] 
for x in fruits:
    if x == "banana":
        continue
    print(x)

#6 The range() function
#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
#Using  
for x in range(6):
    print(x)

#7 
for x in range(2,6):
    print(x)

#8 
for x in range(2, 30, 3): #(start, stop, step)
    print(x)

#9 Else in for loop
for x in range(6):
    print(x)
else:
    print('finally_finished')

#10 
for x in range(6):
    print(x)
    if x == 3:
        continue
else:
    print('finally_finished')

#11 Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits: 
        print(x,y)

#12 The Pass Statement

for x in [0,1,2,]:
    pass

#13 















