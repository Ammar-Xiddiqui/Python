from random import *

SEN = -1
def print_frequency(list):
    print (f'Element\tFrequency')
    for i in range(len(list)):
        count = 1
        for j in range(i+1, len(list)):
            if list[i] != SEN and list[i] == list[j]:
                count += 1
                list[j] = SEN
        if list[i] != SEN:
            print (f'{list[i]} appears {count} times in the list')

def main():
    length = 20
    x = [0]*length
    for i in range(length):
        x[i] = randint(1, 9)
        print (x[i], end = ' ')
    print()
    print_frequency(x)
    print(x)
main()

