#Task 01: Input a character and tell position of bits, which are on in its equivalent binary
# . See sample run
c=input("enter character :")
x=ord(c)
if (x&1)==1: print("bit 1 is on" )
if (x&2)==2: print("bit 2 is on" )
if (x&4)==4: print("bit 3 is on" )
if (x&8)==8: print("bit 4 is on" )
if (x&16)==16: print("bit 5 is on" )
if (x&32)==32: print("bit 6 is on" )
if (x&64)==64: print("bit 7 is on" )
if (x&128)==128: print("bit 8 is on" )
