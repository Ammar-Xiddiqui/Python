'''
enter :5
+
++
+++
++++
+++++
++++
+++
++
+

'''
x=int(input('enter any small number:'))
i=1
while i<=x:
    j=1
    while j<=i:
        print('+',end='')
        j+=1
    print()
    i+=1
    if i>x:
        k=1
        while k<x:
            l=k
            while l<x:
                print("+",end='')
                l+=1
            print()
            k+=1

