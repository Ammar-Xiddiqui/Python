'''
Create three lists of ten elements each. Initialize first two lists with random values in range 1-9. Print 
corresponding elements of first and second list and ask user to add them. Store user’s answers in third list. Check 
user answer is correct or not, calculate score and print score at the end. In the last, print incorrect statements 
and give corresponding correct statement as well
Sample Run:
3 + 5 = 8
2 + 7 = 9
1 + 6 = 5
…
Score 7 / 10
Incorrect       Correct
1 + 6 = 5       1 + 6 = 7
1 + 4 = 6       1 + 4 = 5
'''

from random import*
x=[]
y=[]
z=[]
for i in range(10):
    x.append(randint(1,9))
    y.append(randint(1,9))
print(x)
print(y)
score=0
for i in range(10):
    a=x[i]
    b=y[i]
    print(f'first number is {a} and second number is {b} add them')
    c=int(input('enter answer'))
    if c==a+b:
        score+=1
    z.append(c)
for i in range(10):
    print(f'{x[i]}+{y[i]}={z[i]}')
print(f'score is {score}')
print('incorrect statement\t\tcorrect statement')
for i in range(10):
    if z[i]!=x[i]+y[i]:
        print(f'{x[i]}+{y[i]}={z[i]}\t\t\t\t\t\t{x[i]}+{y[i]}={x[i]+y[i]}')
