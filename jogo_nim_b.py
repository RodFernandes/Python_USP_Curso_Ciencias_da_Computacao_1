import os

def computador_escolhe_jogada(n,m):
    print('computador_escolhe_jogada\n')
    jogada_computador = 1
    while(jogada_computador < m):
        if(jogada_computador == (n % (m + 1) == 0)):
            print('O COmputador tirou ', jogada_computador, ' peça\n')
            return n - jogada_computador
        jogada_computador = jogada_computador + 1
    if(n-m <=0):
        print('O Computador tirou 1 peça\n')
    else:
        print('O Computador tirou ', n - m, ' peça\n')
    return n - m

def usuario_escolhe_jogada(n,m):
    print('usuario_escolhe_jogada')
    retirar_pecas = False
    while(retirar_pecas == False):
        num_pecas = int(input('\nQuantas peças você vai tirar?: '))
        if (num_pecas > m):
            print('\nOops! Jogada inválida! Tente de novo.', 'Maximo por jogada: ', m,'\n')
        else:
            retirar_pecas = True
            if (n - m <= 0):
                print('Você tirou 1 peça\n')
            else:
                print('Você tirou ', num_pecas, ' peça\n')
            print('Você tirou ',num_pecas,' peça\n')
            return n - num_pecas

def checa_multiplos(n,m):
    if (n % (m + 1) == 0):
        return True
    else:
        return False

def config_partida(n,m):
    #Setup da partida
    pass


def game_start():
    pass

def partida():
    print('\n*** Voce escolheu Uma Partida Isolada ***\n')
    #Config
    qtd_pecas = int(input('Quantas peças?: '))
    limite_pecas = int(input('\nLimite de peças por jogada?: '))
    game_ativo = True
    usuario_joga = True
    multiplo = checa_multiplos(qtd_pecas, limite_pecas)
    if (multiplo):
        usuariojoga = True
    else:
        usuario_joga = False


    while(game_ativo):
        if(usuario_joga):
            qtd_pecas = usuario_escolhe_jogada(qtd_pecas, limite_pecas)
            usuario_joga = False
        else:
            qtd_pecas = computador_escolhe_jogada(qtd_pecas, limite_pecas)
            usuario_joga = True

        if (qtd_pecas > 0):
            print('Agora resta apenas ',qtd_pecas ,' peça(s) no tabuleiro.\n')
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

#START_GAME
main()