
# Consider a 2D list/ array of size 9x9. Ignore boundary values that is first and last row & first and last 
# column. Write function to average out remaining values by putting average of eight neighbors. 
# 1 2 8 5 4 7 6 1 6 [For element on second row and second column that is 1, the eight neighbors 
# 9 1 4 1 4 7 8 8 8 are, 1, 2, & 8 in first row. 9 & 4 in second row and 4, 5 & 4 in third row. Their sum 
# 4 5 4 6 8 8 5 6 9 1 + 2 + 8 + 9 + 4 + 4 + 5 + 4 = 37. 37 / 8 = 4. Therefore, you can see the 
# 6 7 3 2 4 9 4 2 9 corresponding value below the line is 4. 
# 8 1 2 2 7 9 4 9 3 
# 5 6 1 8 1 1 5 8 6 
# 1 6 6 2 6 1 5 1 2 
# 8 6 2 2 1 4 1 9 3 
# 8 2 5 5 5 7 3 8 1 
# -------------
# 1 2 8 5 4 7 6 1 6 
# 9 4 4 5 6 6 6 6 8 
# 4 5 4 4 5 6 5 5 9 
# 6 4 3 3 5 6 6 5 9 
# 8 4 4 3 4 4 5 6 3 
# 5 5 4 4 3 3 3 4 6 
# 1 4 4 2 3 2 4 4 2 
# 8 4 3 3 3 4 4 4 3 
# 8 2 5 5 5 7 3 8 1
from random import*
# task 2
x=[[randint(1,9) for i in range(9)]for j in range(9)]
print('list')
for i in range(9):
    for j in range(9):
        print(x[i][j],end=' ')
    print()

print('new list containing changes as per required')

for i in range(1,8):
    sum=0
    for j in range(1,8):
        sum=x[i-1][j-1]+x[i-1][j]+x[i-1][j+1]+x[i][j-1]+x[i][j+1]+x[i+1][j-1]+x[i+1][j]+x[i+1][j+1]
        x[i][j]=sum//8
print()
print()
for i in range(9):
    for j in range(9):
        print(x[i][j],end=' ')
    print()

