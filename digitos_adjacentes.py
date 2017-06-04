numero = int(input('Entre com um numero inteiro:'))
compara = -1
encontrado = False
while(numero > 0):
    x = numero % 10
    if (compara == x):
        encontrado = True
        break
    compara = x
    numero = numero // 10
if (encontrado):
    print('sim')
else:
    print('não')


