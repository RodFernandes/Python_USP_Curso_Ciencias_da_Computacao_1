import math

def main():
    a=float(input('Digite o valor de A:'))
    b=float(input('Digite o valor de B:'))
    c=float(input('Digite o valor de C:'))
    print(bhaskara(a, b, c))

def delta(a,b,c):
    return (b**2)-4*a*c

def bhaskara(a,b,c):
    d = delta(a,b,c)
    print(d)
    if d < 0:
        return('esta equação não possui raízes reais')
    else:
        if d == 0:
            return (-b + math.sqrt(d) / (2*a))
        else:
            #delta > 0
            raiz1 = (-b + math.sqrt(d)) / (2*a)
            raiz2 = (-b - math.sqrt(d)) / (2*a)
            return 'Raiz 1:',raiz1,' Raiz 2:', raiz2

main()
