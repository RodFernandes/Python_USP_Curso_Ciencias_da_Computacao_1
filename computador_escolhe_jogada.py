def checa_multiplos(n,m):
    if (n % (m + 1) == 0):
        return True
    else:
        return False

def computador_escolhe_jogada(n,m):
    print('computador_escolhe_jogada\n')
    jogada_computador = 0
    i = 0
    while(i < m):
        jogada_computador = m - i
        checa_vencedora = n - jogada_computador
        #print(checa_multiplos(checa_vencedora,m))
        if(checa_multiplos(checa_vencedora,m)):
            print('O Computador tirou ', jogada_computador, ' peça\n')
            return jogada_computador
        i = i + 1
    print('O Computador tirou ', m, ' peça\n')
    return m



print(computador_escolhe_jogada(1,1))