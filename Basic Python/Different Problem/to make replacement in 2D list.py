# replace 0 with 1 in 2D list
from random import *

r = 10
c = 10
x = [[randint(0, 9) for j in range(c)] for i in range(r)]
print('list before change')
for a in range(10):
    for b in range(10):
        print(x[a][b], end=' ')
    print()
for i in range(10):
    for j in range(10):
        if x[i][j] == 0: 
            x[i][j] = 1
print()
print( 'list after change')
for c in range(10):
    for d in range(10):
        print(x[c][d], end=' ')
    print()
