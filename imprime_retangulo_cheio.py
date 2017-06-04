largura = int(input('Entre com a largura:'))
altura = int(input('Entre com a altura:'))
a=1
while(a <= altura):
    l = 1
    while(l <= largura):
        print('#',end='')
        l = l + 1
    print('')
    a = a + 1