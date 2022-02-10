# Access Items
#You can access items by referrring to the index number:
from traceback import print_stack


thislist = ['apple', 'banana', 'cherry']
print(thislist[1]) # The first item has an index of 0

# Negative indexing
thislist = ['apple', 'banana', 'cherry']
print(thislist[-1]) #[-1] refers to the last item, [-2]: second to last and so on

# Range of Indexes
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[2:5]) #2 is included but 5 is not

# by leaving out the start of range, it will start at the beginning
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[:4])

# by leaving out the end of range, it will run to the end of the list
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[2:])

#Range of negative indexes
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[-4:-1])

# To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", 'banana', 'cherry']
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

