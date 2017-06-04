def maior_primo(num):
    return éPrimo(num)
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
