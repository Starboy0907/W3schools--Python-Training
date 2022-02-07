# Python Operators
# the add operator
print(10 + 5)
x = 5 
y = 3
print(x+5)

# subtraction
x = 5
x = 3
print(x-y)

# multiplication
x = 5
x = 3
print(x * y)

# Division
x = 12
y = 3
print(x / y)

# Modulus
x = 5
y = 2
print("modulus", x % y)

# Exponentiation
x = 2
x = 5
print(x ** y) #same as 2*2*2*2*2

# Floor Division
x = 15
y = 2
print(x // y) # the floor division // rounds the result down to the nearest whole number

# Assignment Operators
# =
x = 5 
print(x)

# +=
x = 5
x += 3
print(x)

# -=
x = 5
x -= 3
print(x)

# *= 
x = 5
x *= 3
print(x)

# /=
x = 5
x /= 3
print(x)

# %=
x = 5
x %= 3
print(x)

# //=
x = 5
x //=3
print(x)

# &=
x = 5
x &= 3
print(x)

# |=
x = 5
x |= 3
print(x)

# ^= 
x = 5
x^= 3
print(x)

# >>= 
x = 5
x >>= 3
print(x)

# <<=
x = 5
x <<= 3
print(x)

# Python Comparison operators
x = 5
y = 3
print(x == y)
# returns False

x = 5
y = 3
print(x != y)
# returns True. 5 is not 3.

x = 5 
y = 3
print(x > y)
# returns True. 5 is greater than 3. 

x = 5
y = 3
print(x < y)
# returns False because 5 is not less than 3

x = 5
y = 3
print(x >= y)
# returns True. X is greater than 5.

x = 5
y = 3
print(x <= y)
# returns False. X is not equal or less than y.

# Python Logical Operators
# the and operator
x = 5
print(x > 3 and x < 10)
#returns True. X is greater then 3 and 5 is less than 10

# the 
x = 5
print(x > 3 or x < 4)
# returns True. One of the conditions are true (5 is greater than 3)

x = 5
y = 3
print(not(x > 3 and x < 10)) 
# returns False. Not is used in reverse of if.

# Python Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True. x is identical with z.
print(x is y)
# return False. x is not identical with y, though they have the same content.
print(x == y)
# returns True. Though x and y are not identical, they are nontheless, equal.

x = ["apple", "banana"]
print("banana" in x)
# returns True. A sequence with the value "banana" is in the list.

x = ["apple", "banana"]
if "pineapple" not in x:
    print("pineapple is not in x")

'''Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
 ^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off'''














