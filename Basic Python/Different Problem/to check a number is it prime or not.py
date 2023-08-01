# program to input a number and check is it prime number or not
def prime(number):
    if number<2:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
def main():
    while True:
        try:
            x = int(input('enter any integer : '))
            if prime(x):
                print('its a prime number')
            else:
                print('its not a prime number')
            break
        except ValueError:
            print('you have enter a wrong input plz try again')
main()

