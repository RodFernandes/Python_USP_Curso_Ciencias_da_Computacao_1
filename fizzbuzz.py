numero=int(input('Entre com um numero inteiro:'))
if (numero % 3) == 0 and (numero % 5) == 0:
    print('FizzBuzz')
else:
    print(numero)