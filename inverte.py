'''
Exercício 2 - Invertendo sequência

Como pedido na primeira video-aula desta semana, 
escreva um programa que recebe uma sequência de números inteiros terminados por 0 e imprima todos os valores em ordem inversa. 
Note que 0 (ZERO) não deve fazer parte da sequência.
'''

numero = -1
lista = []
while numero != 0:
    numero = int(input('Digite um número:'))
    if numero != 0:
        #lista.append(numero)
        lista.insert(0,numero)

for i in lista:
    print(i)

