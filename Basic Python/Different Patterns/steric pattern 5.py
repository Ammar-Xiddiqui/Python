''' write code to print a pattern like this
Rows: 4
++++++++
+++  +++
++    ++
+      +
++    ++
+++  +++
++++++++

'''
x=int(input('enter :'))
i=1
a=0
while i<=x:
    j=1
    while j<=x-i+1:
        print('+',end="")
        j+=1
#for space
    k=1
    while k<=a:
        print(' ',end='')
        k+=1
    l=1
    while l<=x-i+1:
        print('+',end='')
        l+=1
    print()
    i+=1
    a=a+2
# second part
i=1
a=x*2-4
while i<x:
    j=1
    while j<=i+1:
        print('+',end="")
        j+=1
#for space
    k=1
    while k<=a:
        print(' ',end='')
        k+=1
    l=1
    while l<=i+1:
        print('+',end='')
        l+=1
    print()
    i+=1
    a=a-2



