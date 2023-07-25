# selection sorting for list of 30 numbers , you ma have more element

from random import*
def find_min_index(x,start,end):
    for i in range(start,end):
        if i==start:min_index=i
        elif x[i]<x[min_index]:min_index=i
    return min_index
def main():
    x=[]
    for i in range(30):
        x.append(randint(1,100))
    print(f'list before sorting \n {x}')
    for i in range(30-1):
        min_index=find_min_index(x,i,len(x))
        x[i],x[min_index]=x[min_index],x[i]
    print(f'list after sorting \n {x}')
main()
