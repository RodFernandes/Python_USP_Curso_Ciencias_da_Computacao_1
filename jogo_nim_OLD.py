import os

def computador_escolhe_jogada(n,m):
    comeca = True
    if comeca == True:
        print('Computador começa!')
    else:
        print('computador_escolhe_jogada\n')
    comeca = False
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


def usuario_escolhe_jogada(n,m):
    comeca = True
    if comeca == True:
        print('Voce começa!')
    else:
        print('usuario_escolhe_jogada')
    comeca = False
    retirar_pecas = False
    while(retirar_pecas == False):
        num_pecas = int(input('\nQuantas peças você vai tirar?: '))
        if (num_pecas > m) or (num_pecas <= 0):
            print('\nOops! Jogada inválida! Tente de novo.', 'Maximo por jogada: ', m,' e minimo 1\n')
        else:
            retirar_pecas = True
            print('Você tirou ', num_pecas, ' peça\n')
            return num_pecas


def checa_multiplos(n,m):
    if (n % (m + 1) == 0):
        return True
    else:
        return False

def partida(n):

    if(n == 1):
        print('\n*** Voce escolheu Uma Partida Isolada ***\n')
    else:
        print('\n*** Voce escolheu Um Campeonato ***\n')

    #Config
    game_ativo = True
    usuario_joga = False
    qtd_pecas_max = 0
    limite_pecas = 0
    qtd_pecas_max = int(input('Quantas peças?: '))
    limite_pecas = int(input('\nLimite de peças por jogada?: '))
    '''while(game_ativo == False):
        qtd_pecas_max = int(input('Quantas peças?: '))
        limite_pecas = int(input('\nLimite de peças por jogada?: '))
        if(limite_pecas <= qtd_pecas_max) and (qtd_pecas_max > 0):
            game_ativo =True
        else:
            print('\nValor invalido. Limite de Jogada nao pode ser menor que Quantidade de pecas', qtd_pecas_max,'\n')'''

    qtd_pecas_atual = qtd_pecas_max
    qtd_pecas = 0
    multiplo = checa_multiplos(qtd_pecas_max, limite_pecas)
    if (multiplo):
        usuario_joga = True
    else:
        usuario_joga = False

    while(game_ativo):

        if(usuario_joga):
            qtd_pecas = usuario_escolhe_jogada(qtd_pecas_atual, limite_pecas)
            usuario_joga = False
        else:
            qtd_pecas = computador_escolhe_jogada(qtd_pecas_atual, limite_pecas)
            usuario_joga = True

        qtd_pecas_atual = qtd_pecas_atual - qtd_pecas

        if (qtd_pecas_atual > 0):
            print('Agora resta apenas ',qtd_pecas_atual ,' peça(s) no tabuleiro.\n')
        else:
            print('Fim do jogo!\n')
            if(usuario_joga):
                print('\nO Computador Ganhou\n')
            else:
                print('\nVoce Ganhou!!!\n')
            game_ativo = False


def main():
    cls = lambda: os.system('cls')
    cls()
    print('\n'*5,'Bem vindo ao Game NIM! Escolha:\n \n'
          '1 - Para Jogar Uma Partida Isolada \n'
          '2 - Para Jogar Um Campeonato\n')
    escolha = int(input('Sua escolha: '))
    if(escolha == 1):
        partida(1)
    elif(escolha == 2):
        partida(2)
    else:
        print('Entre com uma opcao valida: 1 ou 2')

def test_partida():
    assert computador_escolhe_jogada(3, 1) == 1
    assert computador_escolhe_jogada(14, 4) == 4
    assert computador_escolhe_jogada(13, 4) == 3
    assert computador_escolhe_jogada(11, 4) == 1
    assert computador_escolhe_jogada(3, 5) == 3
    assert computador_escolhe_jogada(1, 1) == 1
    assert computador_escolhe_jogada(2, 2) == 2

#TEST_GAME
#test_partida()

#START_GAME
main()


