'''
enter :5
+++++
 ++++
  +++
   ++
    +
   ++
  +++
 ++++
+++++
'''
x=int(input('enter any number :'))
i=1
while i<=x:
    j=1
    while j<i:
        print(' ',end='')
        j+=1
    k=1
    while k<=x-i+1:
        print('+',end='')
        k+=1

    print('')
    i+=1
l=1
while l<x:
    m=1
    while m<=x-l-1:
        print(' ',end='')
        m+=1
    n=1
    while n<=l+1:
        print("+",end='')
        n+=1

    print()
    l+=1
