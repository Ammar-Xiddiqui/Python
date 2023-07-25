# function to write first fifty positive even integers 

def even(n):
    if n%2==0:
        for i in range(50):
            print(n,end=' ')
            n+=2
    else:
        n=n+1
        for i in range(50):
            print(n,end=' ')
            n+=2
x=int(input('enter the integer from where the even counting will start'))
even(x)
