'''
Write a program, declare an array of 20 elements. Initialize elements randomly such that each 
element should be larger than previous element. Print the missing values in the list. See sample run 
carefully:
1 3 4 6 7 8 9 13 15 18 20 22 24 26 33 35 37 38 42 45
Output: 
2 5 10 11 14 16 18 19 21 23 27 28 29 30 31 32 34 36 39 40 41 43 44
'''
from random import*
x=[]
a = 1
b = 5
for i in range (20):
    x.append(randint(a,b))
    b += 5
    a = x[i]+1
print(f'this is the orignal list {x}')
for i in range(len(x)-1):
    if x[i]+1!=x[i+1]:
        a=x[i]+1
        while a<x[i+1]:
            print(a,end=' ')
            a+=1
