#to check something present in list or not
from random import*
x=[]
for i in range(10):
    x.append(randint(0,10))
print(x)
def find_num(x,a):
    for i in range(len(x)):
        if x[i]==a:return i
    return -1
def main():
    a=int(input('enter :'))
    print(a)
    v=find_num(x,a)
    if v==-1:print(f'{a} is not present in the list')
    else :print(f'{a} is present in the list')
main()
