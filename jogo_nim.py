def computador_escolhe_jogada(n,m):
    i = 0
    while(i <m):
        jogada_computador = m - i
        vencedora = n - jogada_computador
        if(checa_multiplos(vencedora,m)):
            return jogada_computador
        i = i + 1
    return m

def usuario_escolhe_jogada(n,m):
    concluido = False
    while(concluido == False):
        retirar = int(input('Quantas peças você vai tirar?'))
        if(retirar > m) or (retirar > n) or (retirar <= 0):
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            concluido = True
            return retirar

def campeonato():
    pontos_voce = 0
    pontos_cpu = 0
    rodada = 1
    print('Voce escolheu um campeonato!')
    while(rodada <= 3):
        print('**** Rodada ', rodada, ' ****')
        pontos = partida()
        if (pontos == 1):
            pontos_voce = pontos_voce + 1
        else:
            pontos_cpu = pontos_cpu + 1
        rodada = rodada + 1
    print('**** Final do campeonato! ****')
    print('Placar: Você ',pontos_voce,' X ',pontos_cpu,' Computador')

def partida():
    #print('Voce escolheu uma partida!')
    game_start = False #Checa entradas
    user_starts = False #Define who start the game - User or CPU
    qtd_pecas_current = 0 #Current qtd
    qtd_pecas_return = 0
    #while(game_start == False):
    qtd_pecas = int(input('Quantas peças?'))
    limite_pecas = int(input('Limite de peças por jogada?'))
        #if(qtd_pecas >= limite_pecas):
    game_start = True

    qtd_pecas_current = qtd_pecas
    if (checa_multiplos(qtd_pecas_current, limite_pecas)):
        print('Voce começa!')
        user_starts = True
        #usuario_escolhe_jogada(qtd_pecas, limite_pecas)
    else:
        print('Computador começa!')
        user_starts = False
        #computador_escolhe_jogada(qtd_pecas, limite_pecas)
    #GAME LOOP
    while(game_start == True):
        if(user_starts):
            qtd_pecas_return = usuario_escolhe_jogada(qtd_pecas_current, limite_pecas)
            print('Você tirou',qtd_pecas_return,plural(qtd_pecas_return))
            user_starts = False
        else:
            qtd_pecas_return = computador_escolhe_jogada(qtd_pecas_current, limite_pecas)
            print('O computador tirou',qtd_pecas_return,plural(qtd_pecas_return))
            user_starts = True

        qtd_pecas_current = qtd_pecas_current - qtd_pecas_return

        if(qtd_pecas_current > 0):
            pass
        else:
            game_start = False
            if not(user_starts):
                print('Você ganhou!')
                return 1
            else:
                print('O computador ganhou!')
                return 0

def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('1 - para jogar uma partida isolada')
    opt = int(input('2 - para jogar um campeonato'))
    if opt == 1:
        partida()
    else:
        campeonato()

def plural(n):
    if (n == 1) or (n == -1):
        return 'peça.'
    else:
        return 'peças.'

def checa_multiplos(n,m):
    if (n % (m + 1) == 0):
        return True
    else:
        return False

#START GAME
main()
