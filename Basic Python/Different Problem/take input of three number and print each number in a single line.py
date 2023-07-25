#program to input a three-digit number and print it's digits in single line using integer division and remainde
x=int(input('enter three digit number:'))
print(f'first digit : {x//100}')
x=x%100
print(f'second digit : {x//10}')
print(f'third digit :{x%10}')
