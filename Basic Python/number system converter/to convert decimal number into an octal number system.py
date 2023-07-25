# to convert decimal number into octal number
x=int(input('enter decimal number'))
z=x
r=''
while x!=0:
    a=x%8
    # print(a,end='')
    x=x//8
    r=str(a)+r
print(f'decimal number {z} is equal to {r} but in octal number system')
