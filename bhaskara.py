import math
a=float(input('Digite o valor de A:'))
b=float(input('Digite o valor de B:'))
c=float(input('Digite o valor de C:'))
delta=(b**2)-4*a*c
if delta < 0:
    print('esta equação não possui raízes reais')
else:
    xPositivo = (-b + math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print('a raiz desta equação é', xPositivo)
    else:
        if delta>0:
            xNegativo = (-b - math.sqrt(delta)) / (2 * a)
            print('as raízes da equação são',xNegativo,'e',xPositivo)