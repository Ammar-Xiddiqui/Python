# linear seaarch
from random import*
def main():
    x = []
    for i in range(100):
        x.append(randint(1, 100))
    print(x)
    a = int(input('enter:'))
    for i in range(100):
        if a == x[i]:
            print()
            print(f'{a} is present on {i} position')
            return
    print(f'{a} is not present')
main()
