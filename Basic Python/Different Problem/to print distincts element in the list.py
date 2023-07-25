# : Write code to print distinct elements only in the list
from random import *
x=[]
for i in range(20):
    x.append(randint(1,10))
print('orignal list is ',x)
print('distinct elements in the list are following')
for i in range(20):
    if x[i]!=-1:
        print(x[i], end=' ')
        for j in range(i+1, 20):
            if x[i] == x[j]:x[j]=-1

