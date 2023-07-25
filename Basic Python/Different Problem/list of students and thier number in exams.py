'''
Create a list to store marks of 30 students. Initialize them randomly with marks 0 to 100. Print them in 
single line. Create another list of same size and store roll numbers 1 to 30. Next, at random remove 3-5 students 
by storing sentinel value in the roll no list (you may use -1 as sentinel value). Next, print roll numbers and marks 
column wise. Count the remaining students. Create two more lists according to count and store existing students 
and their roll numbers in the new list. Print new lists (using print(list) statement). See sample run carefully,
78 81 65 72 89 31 …
Roll No Marks
1 78
2 81
3 65
5 89
… 
[1, 2, 3, 5, …
[78, 81, 65, 89, 
'''






x=[]
y=[]
for i in range(20):
    x.append(i+1)
    y.append(randint(1,100))
print(x)
print(y)
a=randint(3,5)
for i in range(a):
    x[randint(0,19)]=-1
print(x)
print(f'roll number\t\t\t\tmarks')
for i in range(20):
    if x[i]!=-1:
        print(f'{x[i]}\t\t\t\t\t{y[i]}')
a=[]
b=[]
for i in range(20):
    if x[i]!=-1:
        a.append(x[i])
        b.append(y[i])
print(a)
print(b)
