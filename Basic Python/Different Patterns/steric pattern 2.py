'''
TO PRINT A PATTERN LIKE THIS
1*2*3
1**2**3
1***2***3
'''

r=int(input('enter '))
i=1
while i<=r:
    j=1
    while j<=r:
        print(j,end='')
        k=1
        if j<r:
         while k<=i:
            print('*',end='')
            k+=1
        j = j + 1
    print()
    i=i+1
