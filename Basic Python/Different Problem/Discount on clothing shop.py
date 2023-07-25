'''
Write a program to calculate discount and net amount paid by the customer if there’s a buying
from a shop and they have following parameters of discount:
Amount    T-Shirts   Pants    Sneakers
0-100         0%      5%        10%
101-200       5%      10%       15%
201-300       10%     15%       20%
Above 300     15%     20%       25%
User have to enter the amount they bought and should categorize T-shirts as t,
pants as p, and sneakers as s.
'''
amount=int(input('enter amount'))
catg=input('enter type')
disc=0
if catg=="t":
    if 0>amount<=100:disc=0
    elif 100>amount<=200:disc=0.05
    elif 200 > amount < 300:disc=0.1
    elif amount>=300 :disc=0.15
elif catg=="p":
    if 0>amount<=100:disc=0.05
    elif 100>amount<=200:disc=0.10
    elif 200 > amount < 300:disc = 0.15
    elif amount>=300 :disc = 0.20
else:
    if 0>amount<=100:disc=0.1
    elif 100>amount<=200:disc=0.15
    elif 200 > amount < 300:disc = 0.20
    elif amount>=300 :disc = 0.25
bill=amount-amount*disc
print(f'amount = {amount}')
print(f'category = {catg}')
print(f'discount = {disc*100}%')
print((f'bill = {bill}'))
