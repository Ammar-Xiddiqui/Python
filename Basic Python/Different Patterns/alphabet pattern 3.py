'''
enter :4

a b c d e 
a c e g i
a d g j m
a e i m q
'''
x=int(input('enter any small interger :'))
c=1
for i in range(1,x+1):
    for j in range(5):
        print(chr(96+c),end=' ')
        c+=i
    print()
    c=1







