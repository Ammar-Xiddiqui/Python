# to find solution of a quadratic equation
def quad(a,b,c): 
    d = (b ** 2 - (4 * a * c)) * 0.5
    e = (-b + d) / 2 * a
    f = (-b - d) / 2 * a
    print(f'x1= {e} and x2= {f}')    
a = int(input('enter a '))
b = int(input('enter b'))
c = int(input('enter c'))
quad(a,b,c)
