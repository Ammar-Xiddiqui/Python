# to print counting in words
def counting_in_words(num):
    ones=['zero','one','two','three','four','five','six','seven','eight','nine',]
    tens=['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    other=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen',]
    if num<10:
        return ones[num]
    elif num<20:
        return other[num-10]
    elif num<100:
        first_digit=num//10
        second_digit=num%10
        if second_digit==0:
            return tens[first_digit-2]
        else :
            return tens[first_digit-2]+' '+ones[second_digit]
    else:return 'hundred'

for num in range(101):
    print(counting_in_words(num))
