''' to print a pattern like this
Rows:5
* * * * 1 * * * * 
* * * 2 * * *
* * 3 * *
* 4 *
5
'''
rows = int(input('Rows:'))
i=1
while i<=rows:
    j=i
    n=rows
    while j<n:
        print('*',end=' ')
        j=j+1
    print(i,end=' ')
    i += 1

    j=i
    while j<=n:
        print('*',end=' ')
        j+=1
    print()
    n -= 1


