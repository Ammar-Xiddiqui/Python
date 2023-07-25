r=int(input('enter any small integer'))
z=r*2
for i in range(1,r+1):
    for a in range(i):
        print(end='*')
    z=z-2
    for b in range(z):
        print(end=' ')
    for c in range(i):
        print(end='*')
    print()
