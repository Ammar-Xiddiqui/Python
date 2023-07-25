import random
j='y'
while j=='y':
    marks = 0
    a = 1
    while a <= 5:
        i1 = random.randint(1, 9)
        i2 = random.randint(1, 9)
        print("Number1  :  ", i1,'       '    "Number2  :  ", i2)
        sum = int(input("Enter Sum of above two numbers : "))
        if (sum == i1 + i2):
            marks = marks + 1
        else:
            sum = int(input("answer  wrong ,enter again: "))
            if (sum == i1 + i2):
                marks = marks + 1
            else:marks=marks
        diff = int(input("Enter difference of above two numbers: "))
        if (diff == i1 - i2):
            marks = marks + 1
        else:
            diff = int(input("Wong answer enter again: "))
            if (diff == i1 - i2):
                marks = marks + 1
            else:marks=marks
        prod = int(input("enter product of above two numbers : "))
        if (prod == i1 * i2):
            marks = marks + 1
        else:
            diff = int(input("Wong answer enter again: "))
            if (prod == i1 * i2):
                marks = marks + 1
            else:marks=marks
        a = a + 1
    print(f'you got score : {marks} out of 15')
    j=input('if you want to play again type \'y\' ')

print('Thanks for playing , hopefully you enjoyed it')

