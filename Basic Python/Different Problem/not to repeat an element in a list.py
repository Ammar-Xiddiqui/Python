'''
Write a program, declare an array of ten elements. Initialize them randomly with values 1 to 
15, where value should not repeat.
'''
from random import *
x=[]
while len(x)<11:
    a=randint(1,15  )
    if a not in x:
        x.append(a)
print(x)
