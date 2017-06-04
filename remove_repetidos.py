'''
Exercício 1 - Removendo elementos repetidos

Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. 
A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

'''

def remove_repetidos(list):
    lista_nova = []

    for i in list:
        exists = False
        for j in lista_nova:
            if i == j:
                exists = True
                break

        if exists == False:
            lista_nova.append(i)

    return sorted(lista_nova)


'''def remove_repetidos(lista):
    lista_nova = []
    for i in lista:
        if len(lista_nova) <= 0:
            lista_nova.append(i)
        else:
            if i != lista_nova.count(i):
                lista_nova.append(i)
 '''

'''def remove_repetidos(lista):
    lista_nova = []
    for i in lista:
        if i != lista_nova.count(i):
            lista_nova.append(i)

    return sorted(lista_nova)
'''

lista = [7,3,33,12,3,3,3,7,12,100]
#lista = [1,2,3]
print(remove_repetidos(lista))