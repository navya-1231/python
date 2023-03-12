
listNew=[1,2,'a','delhi',4.32,5.61]
int_list=[]
float_list=[]
str_list=[]

for i in listNew:
    if type(i)==int:
        int_list.append(i)
    elif type(i)==float:
        float_list.append(i)
    else:
        str_list.append(i)
print(int_list)
print(float_list)
print(str_list)
