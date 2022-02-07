#Python Numbers : int, float, complex

# Int,plex float, com
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float as scientific numbers
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion
x = 1
y = 2.8
z =1j

#convert from int to float
a = float(x)

# convert from float to int
b = int(y)

#convert from int to complex
# you cannot convert complex numbers into another data type

c = complex(x)
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random Number
#python doesnt have a random() but does have a random module that can be used to create random numbers
import random
print(random.randrange(1,10))

