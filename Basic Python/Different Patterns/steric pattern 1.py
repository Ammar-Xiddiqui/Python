# TO PRINT A PATTERN LIKE FOLLOWS
# *
# **
# ***
# ****
# *****
r=int(input('enter rows'))
i=1
a=1
while i<=r:
    j=1
    while j<=a:
        print("*",end="")
        j=j+1
    print()
    if a<r:a=a+1
    i=i+1
