
 # to print a pattern like this
 #     *
 #    * *
 #   *   *
 #  *     *
 # *       *
 #  *     *
 #   *   *
 #    * *
 #     *
r=int(input('enter'))
for i in range(r):
    for a in range(r-i):
        print(end=' ')
    print(end='*')
    for b in range(i*2-1):
        print(end=' ')
    if i==0:print()
    else:print('*')
    k = r * 2 - 5
for i in range(1,r):
    for a in range(i+1):
        print(end=' ')
    print(end='*')
    for b in range(k):
        print(end=' ')
    if i<r-1:  print('*')
    k-=2
print()
