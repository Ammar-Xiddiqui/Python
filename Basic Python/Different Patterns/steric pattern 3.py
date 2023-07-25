# to print * in row and column given by user
r=int(input('enter rows'))
c=int(input('enter column'))
i=1
while i<=r:
    j=1
    while j<=c:
        print('*',end=" ")
        j=j+1
    print()
    i=i+1
