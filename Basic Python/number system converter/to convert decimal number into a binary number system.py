# to convert decimal number into binary number system
x=int(input('enter decimal number'))
r=''
while x!=0:
    a=x%2
    # print(a,end='')
    x=x//2
    r=str(a)+r
print(f'decimal number {x} is equal to {r} but in binary number system')
