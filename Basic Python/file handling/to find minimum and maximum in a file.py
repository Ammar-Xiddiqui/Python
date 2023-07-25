# to find maximum and minimum number in a file
file1=open('prices.txt','r')
a=int(file1.readline())
for i in range(a):
    b=int(file1.readline())
    if i==0:min=max=b
    elif max<b:max=b
    elif min>b:min=b
print(f'maximum number in the file is {max} and minimum is {min}')
file1.close()
