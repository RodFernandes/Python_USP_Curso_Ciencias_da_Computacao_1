largura = int(input('Entre com a largura:'))
altura = int(input('Entre com a altura:'))
a=1
while(a <= altura):
    l = 1
    while(l <= largura):
        if(a == 1) or (a == altura):
            print('#',end='')
        else:
            if(l == 1) or (l == largura):
                print('#', end='')
            else:
                print(' ',end='')
        l = l + 1
    print('')
    a = a + 1