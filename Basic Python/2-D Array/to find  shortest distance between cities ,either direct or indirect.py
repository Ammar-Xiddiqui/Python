'''Print shortest distance between city A and city B. Also print whether 
distance is direct or indirect. In case, of indirect shortest distance print the city number to be used between 
city A and city B.
Sample Runs:
Shortest distance between city 0 and city 7 is 6.
Shortest distance between city 2 and city 5 is 5 via city 4.'''
from random import*
a=[[randint(1,9) for i in range(5)] for j in range(5)]
for i in range(5):
    a[i][i]=0
print(a)
for i in range(5):
    for j in range(5):
        print(a[i][j],end=' ')
    print()
def short(list,c1,c2):
    short_dis=list[c1][c2]
    city=0
    for i in range(len(list)):
        if i!=c1 and i!=c2:
            b=list[c1][i]+list[i][c2]
            if b<short_dis:short_dis=b;city=i
    if city==0:
        print(f'shortest distance between city {c1} and city {c2} is {short_dis}')
    else: print(f'shortest distance between city {c1} and city {c2} via city {city} is {short_dis}')
x=int(input('enter city 1 :'))
y=int(input('enter city 2 :'))
short(a,x,y)
