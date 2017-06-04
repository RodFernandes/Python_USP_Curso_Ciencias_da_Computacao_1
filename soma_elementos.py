'''
Exercício 2 - Soma dos elementos de uma lista

Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.

'''

def soma_elementos(list):
    soma = 0
    for i in list:
        soma = soma + i
    return soma

#lista = [1,2,3,4,5,6]
#print(soma_elementos(lista))