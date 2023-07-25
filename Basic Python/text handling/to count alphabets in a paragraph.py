'''
Read paragraph character by character. Count each alphabet in the paragraph ignoring case. 
(Count capital and small alphabets as the same). Print count of each alphabets for the alphabets appearing in the 
paragraph, if any alphabets is not in the paragraph. Do not display its count. Finally, print total count of 
alphabets and total count of characters in the paragraph:
'''
a=open('paragraph.txt','r')
b=a.readline()
total_character=0
for i in range(26):
    cap=chr(i+65)
    sml=chr(i+97)
    count=0
    for i in range(len(b)):
        if b[i]==cap or b[i]==sml:
            count+=1
    total_character+=count
    print(f'word {cap} is {count} in the paragraph')
print(f'total alphabet in the paragraph are {total_character}')
print(f'total character in the paragraph are {len(b)}')
