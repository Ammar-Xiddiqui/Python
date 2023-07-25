
# to print a pattern like following:
#     1
#    121
#   12321
#  1234321
# 123454321


n=int(input('enter '))
print(f'N:{n}')
for i in range(n):
    for  j in range(n-i-1):
        print (end=' ')
    for  j in range(i+1):
        print (j+1, end='')
    for  j in range(i, 0, -1):
        print (j, end='')
    print()

