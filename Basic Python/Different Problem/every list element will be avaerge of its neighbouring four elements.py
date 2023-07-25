'''
Write a program, declare an array of 20 elements. Initialize elements at random in range 0-9. 
Next, average out each element with value of 4 neighbors. Two neighbors from left side and two from 
right side
'''
from random import*
x=[]
for i in range(20):
    x.append(randint(1,9))
    print(x[i],end=' ')
print()

print(x[0],x[1],end=' ')
for i in range( 2,len(x)-2):
    a=(x[i-1]+x[i-2]+x[i+1]+x[i+2])//4
    print(a,end=' ')
print(x[len(x)-2],x[len(x)-1])

