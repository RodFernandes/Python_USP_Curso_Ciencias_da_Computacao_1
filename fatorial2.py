terminou = False
while(terminou == False):
    numero = int(input('Entre com um numero ou digite um numero negativo para sair:'))
    if(numero < 0):
        terminou = True
    else:
        fat = 1
        i = 1
        while(i <= numero):
            fat = fat * i
            i = i + 1
        print('O Fatorial do numero:',numero,' e: ',fat)
print('*** FIM DO GAME ***')