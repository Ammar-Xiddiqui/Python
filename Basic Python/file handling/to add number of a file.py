# to get sum of numbers of a file
f=open('ammar.txt','r')
loop_controling_variable=int(f.readline())
sm=0
i=1
while i<=loop_controling_variable:
    n=int(f.readline())
    sm += n
    i += 1
f.close()
print(sm)
