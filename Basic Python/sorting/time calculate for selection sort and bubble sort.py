# difference in time in between selection sort and bubble sort
from random import *
from time import *
#Code to calculate sorting time for 10000 elements using bubble sort
def main():
    length = 10000
    x = [0]*length
    for i in range(length):
        x[i] = randint(0, 100000)
    seconds1 = time()
    for j in range(length):
        for i in range(length-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    seconds2 = time()
    print("Time to sort list of 10000 number by bubble sort =", seconds2-seconds1,'sec')
main()




# timing selection sorting 
from random import*
from time import*
def find_min_index(x,start,end):
    for i in range(start,end):
        if i==start:min_index=i
        elif x[i]<x[min_index]:min_index=i
    return min_index
def main():
    x=[]
    for i in range(10000):
        x.append(randint(1,100))
    sec1=time()
    for i in range(10000-1):
        min_index=find_min_index(x,i,len(x))
        x[i],x[min_index]=x[min_index],x[i]
    sec2=time()
    print("Time to sort list of 10000 number by selection sort =", sec2-sec1,'sec')
main()


