# The remove method removes the specified item.

thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)

# Remove Specified Index
# if you do not specify index number, the .pop() method will drop the last list item
thislist = ['apple', 'banana', 'cherry']
thislist.pop(1)
print(thislist)

# You can also remove the specified index with: the del keyword:
thislist = ['apple', 'banana', 'cherry']
del thislist[0]
print(thislist)

# Clear the List
# You can empty the listthe clear method:
thislist = ['apple', 'banana', 'cherry']
thislist.clear()
print(thislist)

