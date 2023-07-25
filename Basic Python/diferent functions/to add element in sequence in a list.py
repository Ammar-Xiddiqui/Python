# to add element in a list but in sequemce

from random import *
 x=[1,2,4,5,6,7,9,13,16,17,18,22,26,28,30]
print(x)
def add_element_in_sequence(list,element):
    for i in range(len(list)): 
        if list[i]>element:
            list.append(' ')
            for j in range(len(list)-1,i,-1):
                list[j]=list[j-1]
            list[i]=element
            break
    else:list.append(element)
    return list
a=15
add_element_in_sequence(x,a)
print(x)
