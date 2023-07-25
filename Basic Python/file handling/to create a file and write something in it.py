# To write counting 1 to 10 in a file
f=open('ammar.txt','w')
i=1
while i<=10:
    f.write(str(i) + '\n')
    i += 1
f.close() 
