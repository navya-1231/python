n=int(input("Enter the number "))
binary=" "
while(n>0):
    rem=n%2
    n=n//2
    binary=str(rem)+binary
print("The binary is",binary)

'''
another method

n=int(input("Enter the number "))
i=0
binary=0
while(n>0):
    rem=n%2
    n=n//2
    binary=10**i*rem+binary
    i=i+1
print("The binary is",binary)

'''