#program to Input a three-digit number and reverse the number by separating digits
x=int(input('enter three digit number:'))
a=(x//100)
#print(f'first digit :{a}')
x=x%100
b=(x//10)
#print(f'second digit :{b}')
c= (x%10)
#print(f'third digit :{c}')
print(f'reverse is {c}{b}{a}')
