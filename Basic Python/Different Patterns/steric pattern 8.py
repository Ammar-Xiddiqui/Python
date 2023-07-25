# to print a pattern like this
'''
enter rows:3
enter column:5
* * * * * >
* * * * * >
* * * * * >
'''
r=int(input('enter rows:'))
c=int(input('enter column:'))
i=1
while i<=r:
    j=1
    while j<=c:
        print('*',end=" ")
        j+=1
        
    print('>')
    i+=1
