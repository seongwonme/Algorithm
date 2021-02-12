a = input()
lalph = 'abcdefghijklmnopqrstuvwxyz'*2
ualph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2

for i in a:
    if i.isupper():
        print(ualph[ualph.find(i)+13], end='')
    elif i.islower():
        print(lalph[lalph.find(i)+13], end='')
    else: 
        print(i, end='')
    
