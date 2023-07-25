# to print three random number in a ascending order
from random import*
x1=randint(1,100)
x2=randint(1,100)
x3=randint(1,100)
print(f'number before ordering {x1,x2,x3}')
if x1>x2:
    x1,x2=x2,x1
if x1>x3:
    x1,x3=x3,x1
if x2>x3:
    x2,x3=x3,x2
print(f'number after ordering {x1,x2,x3}')
