# to print a pattern like this
# enter 5
# **********
# o********o
# oo******oo
# ooo****ooo
# oooo**oooo
# oooo**oooo
# ooo****ooo
# oo******oo
# o********o
# **********

r=int(input('enter '))
a=r*2
def main():
    for i in range(a):
        print(end='*')

main()
b = 1
a-=2
print()
for i in range(r-1):
    for l in range(b):
        print(end='o')
    for m in range(a):
        print(end='*')
    for n in range(b):
        print(end='o')
    b+=1
    a-=2
    print()
b-=1
a+=2
for i in range(r-1):
    for l in range(b):
        print(end='o')
    for m in range(a):
        print(end='*')
    for n in range(b):
        print(end='o')
    b-=1
    a+=2
    print()
main()
