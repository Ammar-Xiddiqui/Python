#Task 04: Input a character and bit position in the equivalent binary of the character from user
# and check, whether the bit is on or off
x=ord(input("enter character :"))
y=int(input("enter bit position :"))
if y==1 and (x&1)==0:
    print("1 bit is off")
elif y==1 and x&1==1:
    print('1 bit is on')

elif y == 2 and (x & 2) == 0:
    print("2 bit is off")
elif y==2 and x & 2 == 2:
    print('2 bit is on')

elif y == 3 and (x & 4) == 0:
    print("3 bit is off")
elif y==3 and x & 4 == 4:
    print('3 bit is on')

elif y == 4 and (x & 8) == 0:
    print("4 bit is off")
elif y==4 and x & 8 == 8:
    print('4 bit is on')

elif y == 5 and (x & 16) == 0:
    print("5 bit is off")
elif y==5 and x & 16 == 16:
    print('5 bit is on')

elif y == 6 and (x & 32) == 0:
    print("6 bit is off")
elif y==6 and x & 32 == 32:
    print('6 bit is on')

elif y == 7 and (x & 64) == 0:
    print("7 bit is off")
elif y==7 and x & 64 == 64:
    print('7 bit is on')

elif y == 8 and (x & 128) == 0:
    print("8 bit is off")
elif y==8 and x & 128 == 128:
    print('8 bit is on')
