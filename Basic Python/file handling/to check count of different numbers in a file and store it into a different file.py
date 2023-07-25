from random import*
with open('nums.txt','w')as f1:
    for i in range(10000):
        f1.write(f'{randint(1,10)}\n')
f=open('nums.txt','r')
i=1
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
sum7=0
sum8=0
sum9=0
sum10=0
while i<=10000:
    n=int(f.readline())
    if n==1:sum1+=1
    if n==2:sum2+=1
    if n==3:sum3+=1
    if n==4:sum4+=1
    if n==5:sum5+=1
    if n==6:sum6+=1
    if n==7:sum7+=1
    if n==8:sum8+=1
    if n==9:sum9+=1
    if n==10:sum10+=1

    i=i+1
f2=open('count.txt','w')
f2.write(f'sum1 are {sum1}\n')
f2.write(f'sum2 are {sum2}\n')
f2.write(f'sum3 are {sum3}\n')
f2.write(f'sum4 are {sum4}\n')
f2.write(f'sum5 are {sum5}\n')
f2.write(f'sum6 are {sum6}\n')
f2.write(f'sum7 are {sum7}\n')
f2.write(f'sum8 are {sum8}\n')
f2.write(f'sum9 are {sum9}\n')
f2.write(f'sum10 are {sum10}\n')
f.close()
f2.close()
