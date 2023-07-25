'''
to print a pattern like this
enter :5
enter :5
1 2 3 4 5 
a b c d e 
2 3 4 5 6 
a b c d e 
3 4 5 6 7 
a b c d e 
4 5 6 7 8 
a b c d e 
5 6 7 8 9 
a b c d e 
'''

r=int(input('enter :'))
c=int(input('enter :'))
con=1
for i in range(1,r+1):
    for j in range(1,c+1):
        print(con,end=' ')
        con+=1
    print()
    con=1
    for k in range(c):
        print((chr(96+con)),end=' ')
        con+=1
    print()
    con=i+1

