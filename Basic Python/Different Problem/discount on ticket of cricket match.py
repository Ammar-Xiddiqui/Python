'''
Qaddafi Stadium has following rates for different type of seats on PSL8
LQ vs KK (Final):

Seat Type           Price
General             1500
First Class         2500
Premium             3000
VIP                 4000
They are giving 10% discount on online booking and 5% on window booking, categorize General as g,
First Class as fc, Premium as p, VIP as v and categorize Online booking as o, window booking as w
'''

name=input('name')
booking_type=input('enter booking type')#online or window
type_of_seat=input("enter seat type")
number_of_ticket=int(input('enter no' ))
if booking_type=='window':
    if type_of_seat=='g':price=1500;disc=0.05
    elif type_of_seat == 'f-c': price = 2500;disc = 0.05
    elif type_of_seat == 'p': price = 3000;disc = 0.05
    elif type_of_seat == 'v': price = 4000;disc = 0.05
elif booking_type=='online':
    if type_of_seat=='g':price=1500;disc=0.1
    elif type_of_seat == 'f-c': price = 2500;disc = 0.1
    elif type_of_seat == 'p': price = 3000;disc = 0.1
    elif type_of_seat == 'v': price = 4000;disc = 0.1
total_disc=disc*price*number_of_ticket
amount=price*number_of_ticket
print(f'name = {name}')
print(f'no. of seats = {number_of_ticket}')
print(f'booking type = {booking_type}')
print(f'type of ticket = {type_of_seat}')
print(f'amount = {amount}')
print(f'discount = {total_disc}')
print(f'amount payable = {amount-total_disc}')

