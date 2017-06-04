numero = int(input('Entre com um numero inteiro:'))
i = 2
while(i <= numero):
    valor = numero % i
    if(valor == 0):
        if(i != numero):
            print('não primo')
            break
        else:
            print('primo')
            break
    i = i + 1