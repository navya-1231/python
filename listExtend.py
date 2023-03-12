lista=[2,4,56,7,89,9]
listb=[100,102,501]
lista.extend(listb)#concatenation using append

lista.sort()#to sort
print(lista)
print("max=",max(lista))#to find max
print("min=",min(lista))#to find min
print("sum=",sum(lista))#to find sum
#concatenation
listc=[1,2,3,5]+[9,8,7]#a new list will be created
print(listc)