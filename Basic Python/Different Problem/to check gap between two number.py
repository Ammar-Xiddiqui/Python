# if two numbers are equal program will print 'equal',if there is a difference of 5 or less between
# number,it will print 'almost equal'otherwise it will print 'not equal'
from random import *
x1=randint(10,30)
x2=randint(10,30)
if x1==x2:
    print(f' marks1 {x1} \n marks2 {x2} \n equal')
elif abs(x1-x2)<=5:
    print(f' marks1 {x1} \n marks2 {x2} \n  almost equal')
elif abs(x1-x2)>5:
    print(f' marks1 {x1} \n marks2 {x2} \n  differnt')
