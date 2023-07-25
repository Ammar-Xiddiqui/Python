# to print a pattern like this 
# 1+2+3+4+5=15
# 1+3+5+7+9=25
# 1+4+7+10+13=35
# 1+5+9+13+17=45




r = int(input())
c = int(input())
i=1
while i<=r:
    j=1
    cont=1
    sum = 0
    while j<=c:
        print(cont, end='')
        sum += cont
        cont += i
        if j < c:
            print('+', end='')
        j += 1
    print(f'={sum}')
    i += 1
