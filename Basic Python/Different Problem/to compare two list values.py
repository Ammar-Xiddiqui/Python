
# Create another list of same size with random numbers. Compare corresponding elements of 
# both lists and for each pair print larger element.
# Sample Run:
# List 1: 23 45 18 17 36
# List 2: 41 14 11 37 46
# 41 45 18 37 46

y=[0]*length
for i in range(length):
    y[i]=randint(1,30)
print(y)
for i in range(length):
    if x[i]>y[i]:
        print(x[i],end=' ')
    else:print(y[i],end=' ')
