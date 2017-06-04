import os

def computador_escolhe_jogada(n,m):
    print('computador_escolhe_jogada\n')
    jogada_computador = 1
    while(jogada_computador < m):
        variavel_temp = (n % (m + 1))
        multiplos = checa_multiplos(n,m)
        #if(jogada_computador == (n % (m + 1) == 0)):
        if (multiplos):
            print('O Computador tirou ', jogada_computador, ' peça\n')
            return jogada_computador
        jogada_computador = jogada_computador + 1
    if(n-m <=0):
        print('O Computador tirou 1 peça\n')
    else:
        print('O Computador tirou ', jogada_computador, ' peça\n')
    return m

def usuario_escolhe_jogada(n,m):
    print('usuario_escolhe_jogada')
    retirar_pecas = False
    while(retirar_pecas == False):
        num_pecas = int(input('\nQuantas peças você vai tirar?: '))
        if (num_pecas > m):
            print('\nOops! Jogada inválida! Tente de novo.', 'Maximo por jogada: ', m,'\n')
        else:
            ''' 
            VERIFICAR PECAS RETIRADAS
            
            '''
            retirar_pecas = True
            if (n - m <= 0):
                print('Você tirou 1 peça\n')
            else:
                print('Você tirou ', num_pecas, ' peça\n')

            print('Você tirou ',num_pecas,' peça\n')
            return num_pecas

def checa_multiplos(n,m):
    if (n % (m + 1) == 0):
        return True
    else:
        return False

def partida():
    print('\n*** Voce escolheu Uma Partida Isolada ***\n')
    #Config
    qtd_pecas_max = int(input('Quantas peças?: '))
    limite_pecas = int(input('\nLimite de peças por jogada?: '))
    game_ativo = True
    usuario_joga = True
    qtd_pecas_atual = qtd_pecas_max
    qtd_pecas = 0
    multiplo = checa_multiplos(qtd_pecas_max, limite_pecas)
    if (multiplo):
        usuariojoga = False
    else:
        usuario_joga = True

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


def campeonato():
    print('\n*** Voce escolheu Campeonato ***\n')
    print('**** Rodada 1 ****')



def main():
    cls = lambda: os.system('cls')
    cls()
    print('\n'*5,'Bem vindo ao Game NIM! Escolha:\n \n'
          '1 - Para Jogar Uma Partida Isolada \n'
          '2 - Para Jogar Um Campeonato\n')
    escolha = int(input('Sua escolha: '))
    if(escolha == 1):
        partida()
    elif(escolha == 2):
        campeonato()
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


