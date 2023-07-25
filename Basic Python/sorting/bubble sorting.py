# bubble sorting for a list of 20 number. you may have more numbers concept will remian same
from random import *
def main():
    x = []
    for i in range(20):
        x.append(randint(0, 100))
    print(f'list before sorting {x}') 
    for j in range(20):
        for i in range(20-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    print(f'list after sorting {x}')
main()
