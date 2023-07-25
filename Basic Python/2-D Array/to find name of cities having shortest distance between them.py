# Print the name of two cities having shortest direct distance

from random import*

a=[[randint(1,9) for i in range(5)]for j in range(5)]
for j in range(5):
    a[j][j]=0
print(a)
for i in range(5):
    for j in range(5):
        print(a[i][j],end=' ')
    print()
short_distance=9
for i in range(5):
    for j in range(5):
        if i!=j:
            b=a[i][j]
            if b<short_distance:short_distance=b;c1=i;c2=j
print(f'shortest distance is between {c1} and {c2} is {short_distance}')

