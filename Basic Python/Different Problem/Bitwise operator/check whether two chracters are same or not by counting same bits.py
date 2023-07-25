#Task 03: Input two characters and check whether they are equal or not by counting same bits in their
# equivalent binary.
x =ord(input('enter the first character:'))
y =ord(input('enter the second character:'))
count=0
if (x&1)==(y&1): count=count+1
if (x&2)==(y&2): count=count+1
if (x&4)==(y&4): count=count+1
if (x&8)==(y&8): count=count+1
if (x&16)==(y&16): count=count+1
if (x&32)==(y&32): count=count+1
if (x&64)==(y&64): count=count+1
if (x&128)==(y&128): count=count+1
if count==8:
    print('numbers are same')
else: print("bits are different")
