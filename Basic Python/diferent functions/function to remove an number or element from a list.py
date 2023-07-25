# to remove any element in a list
from random import*
a=[]
for i in range(30):
    a.append(randint(1,2))
print(a)
def remove_element_from_list(list,element):
    new_list=[]
    for i in range(len(list)): 
        if list[i]!=element:
            new_list.append(list[i])
    list=new_list
    return list
print(remove_element_from_list(a,2))
