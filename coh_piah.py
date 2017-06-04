'''
Funcionamento do programa

Diversos estudos foram compilados e hoje se conhece precisamente a assinatura de um portador de COH-PIAH. 
Seu programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos da seguinte forma:

Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, 
na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). 
Nessa frase, a relação Type-Token vale 45=0.8
Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, 
na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). 
Nessa frase, a relação Hapax Legomana vale 35=0.6
Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças 
(os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
Complexidade de sentença é o número total de frases divido pelo número de sentenças.
Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto 
(os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
Após calcular esses valores para cada texto, você deve comparar com a assinatura fornecida para os infectados por COH-PIAH. 
O grau de similaridade entre dois textos, a e b, é dado pela fórmula:

Sab=∑6i=1||fi,a−fi,b||6

Onde:

Sab é o grau de similaridade entre os textos a e b;
fi,a é o valor de cada traço linguístico i no texto a; e
fi,b é o valor de cada traço linguístico i no texto b.
Perceba que quanto mais similares a e b forem, menor Sab será. Para cada texto, você deve calcular o grau de similaridade com a assinatura do portador de COH-PIAH 
e no final exibir qual o texto que mais provavelmente foi escrito por algum aluno infectado.

'''

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def tam_medio_pal(soma_comp_palavras, num_tot_palavras):
    if num_tot_palavras != 0:
        tam_m_pal = soma_comp_palavras / num_tot_palavras
    else:
        tam_m_pal = 0
    return tam_m_pal


def type_token(lista_palavras, num_tot_palavras):
    num_pal_dif = n_palavras_diferentes(lista_palavras)
    if num_tot_palavras != 0:
        type_token = num_pal_dif / num_tot_palavras
    else:
        type_token = 0
    return type_token


def hapax_lego(lista_palavras, num_tot_palavras):
    num_pal_uni = n_palavras_unicas(lista_palavras)
    if num_tot_palavras != 0:
        h_lego = num_pal_uni / num_tot_palavras
    else:
        h_lego = 0
    return h_lego


def tam_medio_sent(soma_num_cat, num_sent):
    if num_sent != 0:
        tam_m_sent = soma_num_cat / num_sent
    else:
        tam_m_sent = 0
    return tam_m_sent


def compx_med(num_tot_frases, num_tot_sentencas):
    if num_tot_sentencas != 0:
        compx_med = num_tot_frases / num_tot_sentencas
    else:
        compx_med = 0
    return compx_med


def tam_medio_frase(soma_cat_frases, num_tot_frases):
    if num_tot_frases != 0:
        tam_m_frase = soma_cat_frases / num_tot_frases
    else:
        tam_m_frase = 0
    return tam_m_frase

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    lista_Sab = []
    soma_mod = 0
    if type(as_b[0]) is list:
        for lin in range(len(as_b)):
            for col in range(len(as_b[lin])):
                soma_mod += abs(as_a[col] - as_b[lin][col])
            Sab = soma_mod / 6
            lista_Sab.append(Sab)
        return lista_Sab
    else:
        for i in range(len(as_b)):
            soma_mod += abs(as_a[i] - as_b[i])
        Sab = soma_mod / 6
        return Sab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    matriz_ass_input = []
    for i in texto:
        sentencas = []
        sentencas = separa_sentencas(str(i))
        frases = []
        num_tot_sentencas = 0
        soma_cat_sentencas = 0
        for i in range(len(sentencas)):
            frase_i = separa_frases(str(sentencas[i]))
            frases.append(frase_i)
            num_tot_sentencas += 1
            soma_cat_sentencas = soma_cat_sentencas + len(sentencas[i])
        palavras = []
        num_tot_frases = 0
        soma_cat_frases = 0
        for lin in range(len(frases)):
            for col in range(len(frases[lin])):
                palavra_i = separa_palavras(str(frases[lin][col]))
                palavras.append(palavra_i)
                num_tot_frases += 1
                soma_cat_frases = soma_cat_frases + len(str(frases[lin][col]))
        mtrx_para_lista = []
        for lin in range(len(palavras)):
            for col in range(len(palavras[lin])):
                mtrx_para_lista.append(palavras[lin][col])
        palavras = mtrx_para_lista[:]
        soma_comp_palavras = 0
        num_tot_palavras = 0
        for lin in range(len(palavras)):
            for col in range(len(palavras[lin])):
                soma_comp_palavras = soma_comp_palavras + len(str(palavras[lin][col]))
            num_tot_palavras += 1
        ass_txt = []
        ass_txt.append(tam_medio_pal(soma_comp_palavras, num_tot_palavras))
        ass_txt.append(type_token(palavras, num_tot_palavras))
        ass_txt.append(hapax_lego(palavras, num_tot_palavras))
        ass_txt.append(tam_medio_sent(soma_cat_sentencas, num_tot_sentencas))
        ass_txt.append(compx_med(num_tot_frases, num_tot_sentencas))
        ass_txt.append(tam_medio_frase(soma_cat_frases, num_tot_frases))
        matriz_ass_input.append(ass_txt)
    return matriz_ass_input


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    aux_ass_com = (ass_cp[:])
    aux_ass_com.sort()
    for indice in range(len(ass_cp)):
        if aux_ass_com[0] == ass_cp[indice]:
            copiah = indice
    return copiah - 1

def main_teste():
    lista_texto = []
    lista_sentencas = []
    lista_frases = []
    lista_palavras = []
    lista_assinatura = []
    lista_pal_unicas = 0
    lista_pal_diferentes = []

    f = 0
    p = 0

    #lista_assinatura = le_assinatura()
    texto = le_textos()
    for i in texto:
        sentencas = []
        sentencas = separa_sentencas(str(i))
        frases = []
        num_tot_sentencas = 0
        soma_cat_sentencas = 0
        for i in range(len(sentencas)):
            frase_i = separa_frases(str(sentencas[i]))
            frases.append(frase_i)
            num_tot_sentencas += 1
            soma_cat_sentencas = soma_cat_sentencas + len(sentencas[i])
        palavras = []
        num_tot_frases = 0
        soma_cat_frases = 0
        for lin in range(len(frases)):
            for col in range(len(frases[lin])):
                palavra_i = separa_palavras(str(frases[lin][col]))
                palavras.append(palavra_i)
                num_tot_frases += 1
                soma_cat_frases = soma_cat_frases + len(str(frases[lin][col]))
        mtrx_para_lista = []
        for lin in range(len(palavras)):
            for col in range(len(palavras[lin])):
                mtrx_para_lista.append(palavras[lin][col])
        palavras = mtrx_para_lista[:]
        soma_comp_palavras = 0
        num_tot_palavras = 0
        for lin in range(len(palavras)):
            for col in range(len(palavras[lin])):
                soma_comp_palavras = soma_comp_palavras + len(str(palavras[lin][col]))
            num_tot_palavras += 1





            #lista_palavras.append(separa_frases(lista_texto[i]))
    print(sentencas)
    print(frases)
    print(palavras)
    print('Palavras Unicas: ', num_tot_palavras)



    #lista_frases =
    # =
    #lista_pal_unicas = n_palavras_unicas(lista_palavras)
    #lista_pal_diferentes = n_palavras_diferentes(lista_palavras)

#main_teste()
print(calcula_assinatura(le_textos()))