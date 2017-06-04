'''
Exercício 2 - (Difícil) Soma das hipotenusas

Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo n
e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

Dica1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. 
Uma boa solução para este exercício é fazer um laço de 1 até n testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. 
Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

# Para n = 25, as hipotenusas são:
# 5, 10, 13, 15, 17, 20, 25
# note que cada número deve ser somado apenas uma vez. Assim:
soma_hipotenusas(25)
# deve devolver 105


“	Em qualquer triângulo retângulo, a hipotenusa é maior que qualquer um dos catetos, mas menor que a soma deles. [7]	”

O resultado dos testes com seu programa foi:

***** [0.25 pontos]: Soma de hipotenusas ate 6 - Falhou *****
AssertionError: Expected 5 but got 10

***** [0.25 pontos]: Soma de hipotenusas ate 15 - Falhou *****
AssertionError: Expected 43 but got 120

***** [0.25 pontos]: Soma de hipotenusas ate 20 - Falhou *****
AssertionError: Expected 80 but got 210

***** [0.25 pontos]: Soma de hipotenusas ate 27 - Falhou *****
AssertionError: Expected 131 but got 430


'''

import math

def é_hipotenusa(n):
    i = 1
    while(i <= n):
        j = 1
        while(j <= n):
            a = i
            b = j
            c = int(math.sqrt((a ** 2) + (b ** 2)))
            if (c > a) and (c > b) and (c < (a + b)):
                if ((a ** 2) + (b ** 2) == c ** 2):
                    if(c == n):
                        return c
            j = j +1
        i = i + 1

    return 0

def soma_hipotenusas(n):
    soma = 0
    old = 0
    i = 1
    for i in range(1,n+1):
        result = é_hipotenusa(i)
        if(result > old):
            old = result
            soma = soma + result

    return soma
