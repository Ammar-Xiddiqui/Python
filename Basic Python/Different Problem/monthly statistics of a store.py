'''
 Declare a list of 12 elements to store monthly sales. Initialize sale at random with values in range (10-99).
Print sales of each quarter in single line
Sample Run:
Monthly Sales: 11 42 11 32 34 33 40 10 20 24 16 22
 Quarter I: 11 42 11 Min: 11 Max: 42 Average: 21.33
Quarter 2: 32 34 33 Min: 32 Max: 34 Average: 33.00
Quarter 3: 40 10 20 Min: 10 Max: 40 Average: 23.33
Quarter 4: 24 16 22 Min: 16 Max: 24 Average: 20.66
Quarter 3 has minimum sale 10
Quarter 1 has maximum sale 42
Quarter 4 has minimum average sale 20.66
Quarter 2 has maximum average sale 33.00
'''
from random import*
x=[0]*12
for i in range(12):
    x[i]=randint(10,99)
    print(x[i],end=' ')
print()
print(f'first quarter\t',end=' ')
sum=0
for k in range(3):
    if k==0:min=max=x[k]
    print(f'{x[k]}', end=' ')
    sum+=x[k]
    if x[k]<min:min=x[k]
    if x[k]>max:max=x[k]
print(f'\t min is {min}',end=' ')
print(f'\t max is {max}',end=' ')
print(f'\t average is {(sum/3):0.2f}',end=' ')
print()
print(f'second quarter\t',end=' ')
maximum_value=max;b=1
minimum_value=min;a=1
minimum_avg=sum/3;c=1
maximum_avg=sum/3;d=1
sum=0
for k in range(3,6):
    if k == 3: min = max = x[k]
    print(f'{x[k]}', end=' ')
    sum+=x[k]
    if x[k]<min:min=x[k]
    if x[k]>max:max=x[k]
print(f'\t min is {min}',end=' ')
print(f'\t max is {max}',end=' ')
print(f'\t average is {(sum/3):0.2f}',end=' ')
print()
print(f'third quarter\t',end=' ')
if min<minimum_value:minimum_value=min;a=2
if max>maximum_value:maximum_value=max;b=2
if (sum/3)>maximum_avg:maximum_avg=(sum/3);d=2
if (sum/3)<minimum_avg:minimum_avg=(sum/3);c=2
sum=0
for k in range(6,9):
    if k == 6: min = max = x[k]
    print(f'{x[k]}', end=' ')
    sum+=x[k]
    if x[k]<min:min=x[k]
    if x[k]>max:max=x[k]
print(f'\t min is {min}',end=' ')
print(f'\t max is {max}',end=' ')
print(f'\t average is {(sum/3):0.2f}',end=' ')
print()
print(f'fourth quarter\t',end=' ')
if min<minimum_value:minimum_value=min;a=3
if max>maximum_value:maximum_value=max;b=3
if (sum/3)>maximum_avg:maximum_avg=(sum/3);d=3
if (sum/3)<minimum_avg:minimum_avg=(sum/3);c=3
sum=0
for k in range(9,12):
    if k == 9: min = max = x[k]
    print(f'{x[k]}', end=' ')
    sum+=x[k]
    if x[k]<min:min=x[k]
    if x[k]>max:max=x[k]
print(f'\t min is {min}',end=' ')
print(f'\t max is {max}',end=' ')
print(f'\t average is {(sum/3):0.2f}',end=' ')
if min<minimum_value:minimum_value=min;a=4
if max>maximum_value:maximum_value=max;b=4
if (sum/3)>maximum_avg:maximum_avg=(sum/3);d=4
if (sum/3)<minimum_avg:minimum_avg=(sum/3);c=4
print()
print(f'quarter {a} has minimum value{minimum_value}')
print(f'quarter {b} has maximim value{maximum_value}')
print(f'quarter {c} has minimim average{minimum_avg:0.2f}')
print(f'quarter {d} has maximim average{maximum_avg:0.2f}')
