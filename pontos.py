import math
xa=float(input('Entre com o valor de XA:'))
xb=float(input('Entre com o valor de XB:'))
ya=float(input('Entre com o valor de YA:'))
yb=float(input('Entre com o valor de YB:'))
d=math.sqrt(((xb-xa)**2)+((yb-ya)**2))
if d >= 10:
    print('Longe:',d)
else:
    print('Perto:',d)





