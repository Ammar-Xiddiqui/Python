# to print index of 0 in 2D list 
from random import *
r=10
c=10
x = [[randint(0,9) for j in range(c)] for i in range(r)]
for a in range(10):
    for b in range(10):
        print(x[a][b],end=' ')
    print()
print()
for i in range(10):
    for j in range(10):
        if x[i][j]==0:
            print(f'list[{i+1}][{j+1}] is zero')
