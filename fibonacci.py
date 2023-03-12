n=int(input("Enter the number "))
first_no=0
second_no=1
print(first_no)
print(second_no)
for i in range(2,n):#loop starts from 2 because 0 and 1 are already printed
    temp=first_no+second_no
    print(temp)
    first_no=second_no
    second_no=temp
    