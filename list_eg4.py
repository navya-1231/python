numlist=[]
n=int(input("How many numbers: "))
for i in range(n):
    num=int(input())
    numlist.append(num)
print(numlist)
positive_list=[]
negative_list=[]
for i in numlist:
    if i>=0:
        positive_list.append(i)
    else:
        negative_list.append(i)
print("positive numbers are",positive_list)
print("negative numbers are",negative_list)
