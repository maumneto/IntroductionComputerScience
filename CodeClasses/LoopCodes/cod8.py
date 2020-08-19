# Faça um programa que leia um conjunto não determinado de valores e mostre o
# valor lido, seu quadrado, seu cubo e sua raiz quadrada. Finalize a entrada de
# dados com um valor negativo ou zero.
from math import sqrt

while True:
    num = float(input('Digite um valor numérico: '))
    
    if (num <= 0):
        print('Entrada Inválida! Saindo do Loop...')
        break

    print(f'O valor digitado foi {num}')
    quad = num**2 #pow(num, 2)
    print(f'O quadrado do número é: {quad}')
    cubo = num**3
    print(f'O cubo do número é: {cubo}')
    raiz_quad = sqrt(num)
    print('O raiz quadrada do número é: %.2f' % raiz_quad)
    print(' ')

print('Fim!')

