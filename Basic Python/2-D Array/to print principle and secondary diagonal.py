# : Create a 2D list of size 4 x 4. Means, there are four rows and four columns. Initialize elements at 
# random with two-digit numbers. Print elements in single line. Next, print both diagonals in separate lines.
# Sample Run:
# 31 42 73 24 15 96 78 44 62 20 39 58 40 60 54 88
# Principal Diagonal: 31 96 39 88
# Secondary Diagonal: 24 78 20 40
from random import *
x=[[randint(10,99)for i in range(4)]for j in range(4)]
print(x)
for i in range(4):
    for j in range(4):
        print(x[i][j],end=' ')
print()
for i in range(4):
    for j in range(4):
        print(x[i][j],end=' ')
    print()
print(f'\n principle diagonal')
for i in range(4):
    print(x[i][i],end=' ')
print(f'\n secondary diagonal')
for i in range(4):
    for j in range(3,-1,-1):
        if i+j==3:print(x[i][j],end=' ')
