#: Write a program to input card type (a single character D, H, S or C). Print color of the card?
card_type = int(input('enter number :'))
if card_type==0: card_type='DIAMOND';#here 0 represent diamond
elif card_type==1:card_type='HEART';#here 1 represent heart
elif card_type==2:card_type='SPADE';#here 2 represent spade
elif card_type==3:card_type='CLUB';#here 3 represent club
print('cardtrype=',card_type)
if card_type=='DIAMOND' or card_type=='HEART':
    print('red')
else:print('black')
