#Add List Items
#Append Items - to add an item to the end of the list, use the .append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items at a specified index, use the insert() method. The insert() method insert an item at the specified index, use the insert() method.add()

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# The extend() method will append any iterable object
thislist = ["apple", "banana","cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#



