# function to give one vowel as an input and it will give you the next vowel
a=input('enter ')
def vow(a):
    if ord(a) < ord('e'):return('e')
    elif ord(a) < ord('o'):return ('o')
    elif ord(a) < ord('u'):return ('u')
    elif ord(a) < ord('i'): return ('i')
    else: return('a')
print(vow(a))


