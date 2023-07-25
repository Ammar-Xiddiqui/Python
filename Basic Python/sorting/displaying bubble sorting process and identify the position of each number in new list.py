# sorting a list using bubble sort and printing it each time and then telling the position of each number in sorted list

 
from random import *
x=[]
for i in range(10):
    x.append(randint(10,99))
y=[x[i] for i in range(len(x))]
print(f'{y}\n')
for i in range(len(x)):
    for k in range(10):
        print(x[k],end=' ')
    print()
    for j in range(len(x)-1):
        if x[j]>x[j+1]:x[j],x[j+1]=x[j+1],x[j]
print(f'sorted list {x}')
for i in range(10):
    for j in range(10):
        if y[i]==x[j]:
            print(f'{y[i]} is on {j} position')

