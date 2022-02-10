#Join List
#You can join list with the + operator

list1 = ["a","b","c"]
list2 = [1,2,3,]
list3 = list1 + list2
print(list)

# You can append all the items from list2 into list1:
list1 = ["a","b","c"]
list2 = [1,2,3]
for x in list2:
    list1.append(x)
print(list1)

# You can also join listwith the extend method: {list1}.extend{list2}:
list1 = ["a","b","c"]
list2 = [1,2,3]
list1.extend(list2)
print(list1)