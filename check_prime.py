no = 12
flag = False

for i in range(2, (no+1)//2):
    if no % i == 0:
        flag = True
        print('non prime')
        break
else:
    print('prime')
