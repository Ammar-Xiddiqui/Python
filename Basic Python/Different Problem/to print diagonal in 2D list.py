'''
Create a 2D list of size 10 x 10. Initialize value at random in range 0 - 9. Print values in tabular form. 
Next, print principal diagonals only in diagonal form:
'''

from random import *
r=10
c=10
x = [[randint(0,9) for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        print(x[i][j],end=' ')
    print()
for i in range(10):
    for j in range(i):
        print(' ',end='')
    print(x[i][i])
