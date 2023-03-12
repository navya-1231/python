'''
st=input("Enter the string ")
st1=st[::-1]
if(st1==st):
    print("Pallindrome")
else:
    print("not pallindrome")
    '''

st=input("Enter the string ")
st1=" "
for i  in st:
    st1=i+st1
if(st1==st):
    print("Pallindrome")
else:
    print("not pallindrome")