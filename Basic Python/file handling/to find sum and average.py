# to find sum and average of numbers written in a file
file1=open('prices.txt','r')
a=int(file1.readline())
sum=0
for i in range(a):
    b=int(file1.readline())
    sum+=b
print(f'sum of all number in a file is {sum}')
d=sum/a
print(f'average of number in a list is {d}')
file1.close
