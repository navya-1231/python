str="PROGRAMMING IN PYTHON"
f=open("code.text",'w')
f.write(str)
f.close()
f=open("code.text",'r')
f.read()
print(str)
f.close()