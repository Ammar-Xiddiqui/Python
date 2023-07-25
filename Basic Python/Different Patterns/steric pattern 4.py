#to print a 'w' of steric 

r=int(input('enter rows '))
a=r*2-2
for i in range(1,r+1):
    for j in range(1,i+1):
        print(' ',end='')
    print("*",end='')
    for k in range(1,a):
        print(' ',end='')
    if i<r:
           print('*',end='')
    for j in range( 2,i+1 ):
        print(' ', end=' ')
    if j>1 :
     print('*',end='')
    else :print('',end='')
    for k in range(1,a):
        if i==1 and k==1:print(' ',end='')
        print(' ',end='')
    if i<r:
          print('*')
    a-=2
