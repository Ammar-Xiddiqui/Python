# to print rectangle of steric *
def rect(a,b):
    for i in range(1):
        for j in range(c):
            print('*', end='')
        print()
    for i in range(r - 2):
        print("*", end='')
        for j in range(c - 2):
            print(' ', end='')
        print('*')
    for i in range(1):
        for j in range(c):
            print('*', end='')
        print()
r = int(input('enter an interger higher than 2 (for height of rectangle): '))
c = int(input('enter an interger higher than 2 (for width of rectangle):'))
rect(r,c)
 
