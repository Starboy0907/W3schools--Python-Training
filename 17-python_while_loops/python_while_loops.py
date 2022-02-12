#1 The While Loop
    #With the while loop, you can ececute a set of statements as long as a condition is true

i = 1 # Set the iterator to 1, as while loops require the variables to be ready
while i < 6: #condition
    print(i) #print i through each loop 
    i += 1  #incrementing statement is needed to preventing never-ending loop 

#Continue Statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#The else Statement
# you can execute a block of code with the condition is no longer true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")





