'''
enter rows:5
enter column:5
(1,1),(1,2),(1,3),(1,4),(1,5),(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(3,4),(3,5),(4,1),(4,2),(4,3),(4,4),(4,5),
(5,1),(5,2),(5,3),(5,4),(5,5)

'''
r=int(input('enter rows:'))
c=int(input('enter column:'))
i=1
while i<=r:
    j=1
    while j<=c:
        print(f'({i},{j})',end="")
        if i<r or j<c:
            print(',',end='')
        j=j+1
    i+=1
