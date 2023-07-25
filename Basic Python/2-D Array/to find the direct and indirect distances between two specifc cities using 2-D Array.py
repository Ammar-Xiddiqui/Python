'''
Write a function with three parameters distance, city 1 and city 2. The distance is the 2D list (given), city 1 
and city 2 is some number from 0 to LENGTH - 1. Print all distances from city 1 to city 2. One distance will be 
direct. Remaining distances will be one indirect. For example, there will be one direct distance between city 
2 and city 4; whereas, there will be a distance between city 2 and city 4 via city 2 to city 6 and city 6 to city 2 
and the total distance will be the sum of two distances. '''


from random import*

a=[[randint(1,9) for i in range(5)] for j in range(5)]
for i in range(5):
    a[i][i]=0
print(a)
for i in range(5):
    for j in range(5):
        print(a[i][j],end=' ')
    print()
def dis(list,city1,city2):
    print(f'direct distance between city {city1} and city  {city2} is {list[city1][city2]}')
    for i in range(len(list)):
        if  city1!=i and city2!=i:
            print(f'indirect distance between city {city1} and city {city2} via city {i} is {list[city1][i]+list[i][city2]}')
dis(a,randint(0,4),randint(0,4))
