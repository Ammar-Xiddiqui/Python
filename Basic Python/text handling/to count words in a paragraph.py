'''
Count words in the paragraph. The character to separate the words is space, full stop and comma. Also 
count and print words starting from each alphabets (if they are not zero, means do not display zero count). At 
the end print total sum of individual count, which should tally (match) with total word count.'''


a=open('paragraph.txt','r')
p=a.readline()
w_c=0
for i in range(len(p)):
    if p[i]==' ' or i==len(p)-1 :
        w_c+=1
print(w_c)
sum=0
for i in range(26):
    cap = chr(i + 65)
    sml = chr(i + 97)
    num=0
    a_c=0
    for j in range(len(p)):
        if p[j] == ' ' or j==len(p)-1:
            if p[j-num]==cap or p[j-num]==sml :
                a_c += 1
            num = 0
        else:num+=1
    sum+=a_c
    if a_c>0:
        print(f'{a_c} words start from {cap}')

print(sum)
a.close
