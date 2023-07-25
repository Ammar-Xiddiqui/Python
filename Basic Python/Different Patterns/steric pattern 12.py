# to print a pattern like this
# enter rows 5
# enter column 5
# ooooo     ooooo
#      o   o
#       o o
#        o
#       o o
#      o   o
# ooooo     ooooo

r=int(input('enter rows '))
c=int(input('enter column '))
if r%2==0:r+=1
for i in range(c):print(end='o')
for i in range(r):print(end=' ')
for i in range(c):print(end='o')
print()
space1=c
space2=r-2
for i in range(1,r,2):
    for i in range(space1): print(end=' ')
    for i in range(1): print(end='o')
    for i in range(space2): print(end=' ')
    for i in range(1): print(end='o')
    space1+=1;space2-=2
    print()
for i in range(1):
    for i in range(space1):print(end=' ')
    print('o')
space1-=1
space2+=2
for i in range(1,r,2):
    for i in range(space1):print(end=' ')
    print(end='o')
    for i in range(space2):print(end=' ')
    print('o')
    space1-=1
    space2+=2

for i in range(c):print(end='o')
for i in range(r):print(end=' ')
for i in range(c):print(end='o')
