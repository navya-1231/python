num=int(input("How many names"))
list_new=[]
print("Enter the names")
for i in range(num):
    name=input()
    list_new.append(name)
list_new.sort()
print(list_new)


