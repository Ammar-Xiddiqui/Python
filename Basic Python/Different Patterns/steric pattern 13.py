
# task 7
# to print a pattern like this
# enter : 5
#  \ 
#   \ 
#    \ 
#     \ 
#      \  _ _ _ _ _ 
#      /
#     /
#    /
#   /
#  /

r=int(int(input('enter : ')))
for i in range(r):
    for j in range(i+1):print(end=' ')
    if i<r-1:
      print('\ ')
    if i==r-1:print('\ ',end=" ")
for i in range(r):print('_',end=' ')
print()
for i in range(1,r+1):
    for j in range(r-i):
        print(end=' ')
    print(' /')
#
