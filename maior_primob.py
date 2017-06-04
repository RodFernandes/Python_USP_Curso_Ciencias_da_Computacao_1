a = int(input('Digite o primeiro valor:'))


def maior_primo(num):
    # if (num >= 2):
    pass


def éPrimo(k):
    i = 2
    aux = 1 #
    primo = -1
    while (i <= k):
        valor = k % i
        if (valor == 0):
            aux = aux + 1
            if (aux >= 3):
                k = k -1
                aux = 1
                i = 2
            primo = i
        i = i + 1
    return primo



print(éPrimo(a))

# maior_primo(a)
