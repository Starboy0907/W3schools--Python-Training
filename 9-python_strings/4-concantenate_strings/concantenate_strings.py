# String Concantenation
# Merge variable a with varible b into variable c:
a = "Hello "
b = "World!"
c = a + b
print(c)

# Adding a space in concantenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# this will produce a TypeError
age = 36
txt = "My name is John, I am " + age
print(txt)

# But we can combine strings and numbers by using the format() method and placing passed argument where the placeholders {} are. 
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# the format method takes unlimited arguments
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of an item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Use can use index numbers to make sure that the right variable are being passed into to the intended placeholders.
quantity = 3
itemno = 567
price = 49.95 
myorder = "I want to pay {2}, dollars for {0} pieces of item{1}"


