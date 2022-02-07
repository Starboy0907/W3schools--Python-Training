# Escape Character
# the below syntax will produce an SyntaxError
#txt = "We are the so-called "Vikings" from the north."

txt = "We are the so-called \"Vikings\" from the North"
print(txt)

#single quote
txt = 'It\'s Alright'
print(txt)

#backslash
txt = "This will insert one \\ (backslash)."
print(txt)

#newline
txt = "Hello\nWorld!"
print(txt)

#carriage return
txt = "Hello\rWorld!"
print(txt)

#tab
txt = "Hello\tWorld!"
print(txt)

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)



