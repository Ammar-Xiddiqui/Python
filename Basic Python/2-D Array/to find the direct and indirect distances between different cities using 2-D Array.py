from random import *

# ALL DISTANCES BETWEEN CITIES (DIRECT AND INDIECT)
a=[[randint(1,9) for i in range(5)] for j in range(5)]
for i in range(5):
    a[i][i]=0
print(a)
print('\tcity1\tcity2\tcity3\tcity4\tcity5')
print()
for i in range(5):
    print(f'city {i+1}\t',end=' ')
    for j in range(5):
        print(a[i][j],end='\t ')
    print()
for i in range(5):
    for j in range(5):
        if i!=j:
            print(f'direct distance between city {i+1} to city {j+1} is {a[i][j]}')
            for k in range(5):
                if i != k and j != k:
                    print(f'indirect distance between city {i+1} and city {j+1 } via city {k+1} is {a[i][k] + a[k][j]}')
