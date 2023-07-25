# PROGRAM TO PRINT ODD AND EVEN BETWEEN TWO GIVEN NUMBER
x=int(input('enter starting number')) 
y=int(input('enter ending number'))
print(f'even number between {x} and {y} are :',end=' ')
for i in range(x,y+1):
    if i%2==0:print(i,end=' ')
print()
print(f'odd number between {x} and {y} are :',end=' ')
for i in range(x,y+1):
    if i%2==1:print(i,end=' ')
