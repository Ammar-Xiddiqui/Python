#to count words in pragraph



x="life, living matter and, as such, matter that shows certain at tributes that \
include responsiveness, growth, metabolism, energy transformation, and reproduction. \
Although a noun, as with other defined entities, the word life might be better cast as \
a verb to reflect its essential status as a process. Life comprises individuals, living \
beings, assignable to groups (taxa). Each individual is composed of one or more minimal \
living units, called cells, and is capable of transformation of carbon-based and other \
compounds (metabolism), growth, and participation in reproductive acts. Life forms \
present on Earth today have evolved from ancient common ancestors through the generation \
of hereditary variation and natural selection. The several branches of science \
that reveal the common historical, functional, and chemical basis of the evolution of all \
life include electron microscopy, genetics, paleo biology (including paleontology), and \
molecular biology."





w_c=0
for i in range(len(x)):
    if x[i] != ',' or x[i] != '(' or x[i] != ')'or x[i]!='.' :
        if x[i]==' ' or i==len(x)-1:
            w_c+=1
print('total words in paragraph are ',w_c)


l_w=0
p=0
n_w=0
sum=0
for i in range(len(x)):
    if x[i] != ',' or x[i] != '(' or x[i] != ')' or x[i] != '.':
        if x[i] == ' ' or i==len(x) :
            if sum>l_w: l_w=sum; n_w=p;
            p += 1
            sum = 0
        else:
            sum+=1
print(f' and word {n_w}  is longest word as it has {l_w}  alphabets')
