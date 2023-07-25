# to print a pattern like this
# A 1 B 1 2 C 1 2 3 D 1 2 3 4 E 1 2 3 4 5 
# F 1 G 1 2 H 1 2 3 I 1 2 3 4 J 1 2 3 4 5
# K 1 L 1 2 M 1 2 3 N 1 2 3 4 O 1 2 3 4 5
# P 1 Q 1 2 R 1 2 3 S 1 2 3 4 T 1 2 3 4 5
# U 1 V 1 2 W 1 2 3 X 1 2 3 4 Y 1 2 3 4 5


r=int(input ('enter '))
i=1
count=1
while i<=r:
    j=1
    while j<=r:
        print(chr(64+count),end=" ")
        k = 1
        num=1
        while k <=j :
            print(k, end=' ')
            k += 1
        j = j + 1
        count+=1
    print()
    i+=1
