'''
enter rows:3
enter column:3

1       1
1       2
1       3
2       1
2       2
2       3
3       1
3       2
3       3
'''
r=int(input('enter rows:'))
c=int(input('enter column:'))
i=1
while i<=r:
    j=1
    while j<=c:
        print(f'{i}       {j}')
        j=j+1
    i+=1
