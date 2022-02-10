list1 = ['a','b','c']
list2 = [1,2,3,4]
list1.append('d')
print(list1)
list2.clear()
print(list2)
print(list2.count(list2))
list2.append(4)
print(list2)
list1.extend(list2)
print(list1)
print(list2.index(4))
list2.insert(1, 5)
print(list2)
list1.pop(2)
print(list1)
list1.remove(0)
list2.reverse()
print(list2)
list1.sort()
print(list1)






