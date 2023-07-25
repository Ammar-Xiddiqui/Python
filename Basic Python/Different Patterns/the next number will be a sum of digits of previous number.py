x = 1
i = 1
while i<=99:
    left=(x//10)
    right=(x%10)
    third_right = (left+right)%10
    third_left = (left+right)//10
    if x//10 ==0:
        print(f'[{x}]',end=" ")
    elif(x//10!=0):
        if((left+right)//10)!=0:
            print(f'[{x} {left+right} {third_left+third_right}]',end=" ")
        else:
            print(f'[{x} {left+right}]',end=" ")
    x = x+1
    i=i+1
