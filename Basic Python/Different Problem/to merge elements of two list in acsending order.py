'''Take two arrays of five elements each, where elements are in ascending order. Create another 
array of 10 elements. Write code to merge previous two arrays into new array in ascending order
'''
from random import*
x=[randint(1,100)for i in range(5)]
y=[randint(1,100)for i in range(5)]
def sort(list):
        y.sort()
print(f'{x}\n{y}')
z=[]
for i in range(10):
    if i<5:
        z.append(x[i])
    else:z.append(y[i-5])
print(z)
z.sort()
print(z)
