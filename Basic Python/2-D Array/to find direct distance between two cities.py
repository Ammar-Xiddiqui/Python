# task 4
# place -1 at random showing there is no direct path between two cities. For example,
# 0 4 -1 6
# 5 0 7 -1
# -1 3 0 -1
# Write code to print cities having direct link
from random import*
x=[[randint(1,9)for i in range(5)]for j in range(5)]
for j in range(5):
    x[j][j]=0
a=randint(4,6)
i=0
while i<=a:
    b=randint(0,4)
    c=randint(0,4)
    if x[b][c]!= 0 and x[b][c]!= -1:
        i+=1
        x[b][c] = -1
for i in range(5):
    for j in range(5):
        print(x[i][j],end=' ')
    print()

for i in range(5):
    print(f'city {i} has direct link with city', end=' ')
    for j in range(5):
        if x[i][j]!=0 and x[i][j]!=-1:
            print(f'{j}',end=' ')
    print()
