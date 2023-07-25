'''
Write a program, declare an array of ten elements. Initialize them randomly with values 1 to 5. 
Check and print index of same element exists at different locations.
'''
from random import *
x=[]
for i in range(10):
    x.append(randint(1,5))
print(x)
for i in range(10):
    if x[i]!=-1:
        print(f'{x[i]} is on {i} place')
        for j in range(i + 1, 10):
            if x[i] == x[j]: x[j] = -1;print(f'{x[i]} is also on {j} place')

