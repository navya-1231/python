word=input("enter a word :")
dist=int(input("Enter the distance value :"))
ciphertext=" "
plaintext=" "
for ch in word:
    ordvalue=ord(ch)
    ciphervalue=ordvalue+dist
    if ciphervalue>ord('z'):
        ciphervalue=(ord(ch)+dist-97)%26+97
    ciphertext+=chr(ciphervalue)
    
print("The cipher word is",ciphertext)
'''
for i in ciphertext:
    ordvalue=ord()
    cvalue=ordvalue=ordvalue-dist
    if cvalue<ord('a'):
        cvalue=(ord(ch)-dist+97)%26-97
    plaintext+=chr(cvalue)
print("The plain text is",plaintext)
'''