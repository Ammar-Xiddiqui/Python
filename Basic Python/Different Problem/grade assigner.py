# to assign a grade to the numbers
from random import*
x1=randint(1,100)
if 85<=x1<=100:
 print(f'marks   {x1} \n grade  a+')
elif  80<=x1<85:
 print(f'marks   {x1} \n grade  a-')
elif 75<=x1<80:
 print(f'marks   {x1} \n grade  b+')
elif 70<=x1<75:
 print(f'marks   {x1} \n grade  b')
elif 65<=x1<70:
 print(f'marks   {x1} \n grade  b-')
elif 61<=x1<65:
 print(f'marks   {x1} \n grade  c+')
elif 58<=x1<61:
 print(f'marks   {x1} \n grade  c')
elif 55<=x1<58:
 print(f'marks   {x1} \n grade  c-')
elif 50<=x1<55:
 print(f'marks   {x1} \n grade  d')
elif x1<50:
 print(f'marks   {x1} \n grade  f')

