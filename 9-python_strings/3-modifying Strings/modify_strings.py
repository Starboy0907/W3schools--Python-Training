# Modifying Strings

#upper case
a = "Hello, World!"
print(a.upper())

# lowercase
a = "Hello, World!"
print(a.lower())

# remove Whitespace
# The strip() method removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip()) #returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Slpit String
# The split method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(",")) #returns ["Hello" , "World"]
