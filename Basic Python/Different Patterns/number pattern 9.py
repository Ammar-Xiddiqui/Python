'''to print a pattern like this
enter 4
1 2 3 4 
1 2 3
1 2
1
'''
x=int(input('enter '))
i=1
while i<=x:
    j=i
    k=1
    while j<=x:
        print(k,end=' ')
        k+=1
        j=j+1

    print()
    i+=1
