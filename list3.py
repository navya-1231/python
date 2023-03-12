"""list_new=[]
print("initial list",list_new)
list_new.append(30)#modify internal structure only
print("new list is",list_new)"""

listA=[1,2,3,4,5,6,7]
print(listA.count(2))
listA.insert(2,5)
print(listA)
print(listA.pop(2))
listA.remove(2)
print(listA)