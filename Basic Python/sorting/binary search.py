# binary search
from random import*
def binary(list,value):
    start=0
    end=len(list)-1
    while start<=end:
        middle=(start+end)//2
        if value==list[middle]:return middle+1
        elif value>list[middle]:start=middle+1
        else:end=middle-1
    return -1
v=[]
for i in range(30):
    v.append(randint(1,100))
    v.sort()
print(v)

y = randint(1, 100)

if binary(v, y) != -1:
    print(f'the value is on {binary(v, y)}')
else:
    print(f'value {y} is not existed')
