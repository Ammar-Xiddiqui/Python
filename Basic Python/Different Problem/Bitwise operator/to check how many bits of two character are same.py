#Task 02: Input two characters and tell how many bits are same in their equivalent binary
x=ord(input('enter character :'))
y=ord(input('enter character :'))
count=0
if (x&1)==(y&1): count=count+1
if (x&2)==(y&2): count=count+1
if (x&4)==(y&4): count=count+1
if (x&8)==(y&8): count=count+1
if (x&16)==(y&16): count=count+1
if (x&32)==(y&32): count=count+1
if (x&64)==(y&64): count=count+1
if (x&128)==(y&128): count=count+1
print(f'in {chr(x)} and {chr(y)} {count} bits are same')
