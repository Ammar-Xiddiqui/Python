'''
Write a program to declare an array of ten elements. Initialize them randomly in any range. 
Print even and odd elements in separate rows. Count both elements. If there are more even elements, 
make all elements even by adding one or if there are more odd elements, make all elements odd by 
subtracting one. At the end print all elements in a single line.

'''
from random import*
x=[randint(1,100)for i in range(20)]
print(x)
even=0
odd=0
for i in range(20):
    if x[i]%2==0:even+=1
    else:odd+=1
print(f'list has {even} even numbers\nlist has {odd} odd numbers')
if even >odd:
    print("even values are greater")
    for i in range(20):
        if x[i]%2==1:
            x[i]+=1
elif even==odd:
    print("odd values are same as even values")
    print(f'list after editing\n{x}')

elif even<odd:
    for i in range(20):
        if x[i]%2==0:
            x[i]-=1
    print("odd values are greater")
    print(f'list after editing\n{x}')
