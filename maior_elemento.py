'''
Exercício 1 - Maior elemento de uma lista

Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e 
devolve um número inteiro correspondente ao maior valor presente na lista recebida.

'''

def maior_elemento(lista):
    maior = lista[0]

    for i in lista:
        for j in lista:
            if i < j:
                maior = j

    return maior


#lista = [1,2,3,5,8,9,4]
#lista = [1]
#print(maior_elemento(lista))