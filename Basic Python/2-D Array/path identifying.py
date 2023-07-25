
# Consider a 2D list/ array of size 9x9, initialized with ones and zeros. Ones indicates path and zero
# indicates a hurdle. It is given that first value at 0, 0 is always 1. Write a function print path from 0, 0 to 8, 8.
# If there exist a path, otherwise print the maximum possible path.
# See example:
# 1 0 0 1 0 1 1 0 0
# 1 0 0 0 0 1 0 0 0
# 1 0 0 0 1 1 1 1 1
# 1 0 0 0 0 1 0 0 0
# 1 0 0 0 1 0 1 0 0
# 1 1 1 1 1 1 1 1 1
# 0 1 1 0 0 1 1 1 1
# 0 0 1 1 1 1 1 1 1
# 0 1 1 1 0 1 1 1 1
# Here, you can see a clear path exists from 0, 0 to 8, 8.


from random import *
x=[[randint(0,1)for i in range(9)]for j in range(9)]
x[0][0]=1
for i in range(9):
    for j in range(9):
        print(x[i][j],end=' ')
    print()
def main(x):
    i=0
    j=0
    while True:
        if i==len(x)-1:
            break
        print(f'{i},{j}-', end='')
        if i<len(x) and x[i+1][j]==1:
            i+=1
        elif j<len(x) and x[i][j+1]==1:
            j+=1
        else:break
    print(f'{i},{j}-', end='')
    if i < len(x)-1 :
        print(f'path blocked')
main(x)
