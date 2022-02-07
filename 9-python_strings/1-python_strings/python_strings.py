# you can use double or single qoutes
print("Hello")
print('Hello')

#Assign a string to a variable
a = "Hello"
print(a)

# Multiline Strings
a = """Loren ipsum dolor sit amet,
consecutor adipiscing elit,
sed do eiumod tempor incididunt
ut labores et dolore magna aliqua"""
print(a)

a = a = '''Loren ipsum dolor sit amet,
consecutor adipiscing elit,
sed do eiumod tempor incididunt
ut labores et dolore magna aliqua'''
print(a)

# Strings are Arrays
# Get the character  at position 1
a = "Hello, World!"
print(a[1])

#Loop through a string
for x in "banana":
    print(x)

# Use the length function to get the length of a string
a = "Hello, World!"
print(len(a))

# Use the keyword in to check if a certain phrase or character is present in a string
txt = "The best things in lofe are free"
print("free" in txt)

# use it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword NOT IN
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is not present")

