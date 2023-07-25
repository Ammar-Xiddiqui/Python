
# Write code to print cities having no direct link but one indirect link.
# Sample Run:
# City 0 has indirect link with 4 via 2

from random import*
x=[[randint(1,9)for i in range(5)]for j in range(5)]
for j in range(5):
    x[j][j]=0
a=randint(4,6)
i=0
while i<=a:
    b = randint(0, 4)
    c = randint(0, 4)
    if x[b][c]!=0 and x[b][c]!=-1:
        x[b][c]=-1
        i+=1

for i in range(5):
    for j in range(5):
        print(x[i][j],end=' ')
    print()
for i in range(5):
    for j in range(5):
        if x[i][j]==-1:
            count=0
            for k in range(5):
                if i!=k and j!=k:
                    if x[i][k]!=-1 and x[k][j]!=-1:
                        count+=1
                        c1=i;c2=j;via=k
            if count == 1:
                print(f'city {c1} and city {c2} has indirect link via {via}')

