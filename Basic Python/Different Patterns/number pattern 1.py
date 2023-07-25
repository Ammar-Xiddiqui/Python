# to print a pattern like this 
# 12345= 15
# 123456= 21
# 1234567= 28
r=int(input('enter rows'))
i=1
count=0
while i<=r:
    j=1
    while j<=i+4:
        print(j,end="")
        count=count+j
        j=j+1
    print("=",count)
    i=i+1
    count=0
