# Exercise:
# Print i as long as i is less than 6.

# 2
i = 1
while i < 6:
    print(i)
i += 1
print(i)

#Exercise 2:
#Stop the loop if i is 3.
i = 1
while i < 6:
    i =+ 1
    if i == 3:
        print(i)

#Exercise3:
#In the loop, when i is 3, jump directly to the next iteration.

i = 0             #set the iterator
while i < 6:      # while condition
    i += 1        #incrementing value
    if i == 3:    # if condition
        continue  # skips this iteration
    print(i)      #prints iterations

#Exercise4:
#Print a message once the condition is false.


i = 1             #set the iterator's value
while i < 6:      # while conditional
    print(i)      # print iterations
    i += 1        # set the incrementing value
else:
    print("i is no longer less than 6")
    
