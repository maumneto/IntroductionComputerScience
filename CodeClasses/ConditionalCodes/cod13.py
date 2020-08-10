# Faça um programa (menu.py) que mostre o menu de opções a seguir, receba a opção do usuário e os
# dados necessários para executar cada operação. 
# python3 menu.py
# Menu de opções
# 1 - Somar dois números
# 2 - Dividir dois números
# 3 - Raiz quadrada de um número
# Digite a sua opção:
# No caso da operação 2, o segundo número não pode ser zero.
# No caso da operação 3, o número não pode ser negativo.
# Se a opção digitada for inválida, mostre uma mensagem de erro.

# import math
from math import sqrt

print('Menu de Opções\n[1]-SOMA\n[2]-DIVIDE\n[3]-RAIZ QUADRADA')
option = int(input('Digite sua opção: '))

if (option == 1):
    number1 = float(input('Digite o primeiro valor: '))
    number2 = float(input('Digite o segundo valor: '))
    soma = number1 + number2
    print('O resultado da soma é: %.2f' % soma)
elif (option == 2):
    number1 = float(input('Digite o primeiro valor: '))
    number2 = float(input('Digite o segundo valor: '))
    if ( number2 == 0 ):
        print('Não é possível divisão por zero!')
    else:
        divCalc = number1 / number2
        print('O resultado da divisão é %.2f' % divCalc)
elif (option == 3):
    number1 = float(input('Digite um valor positivo: '))
    if ( number1 < 0 ):
        print('Não é possível raiz quadrada de negativos')
    else:
        squareRoot = sqrt(number1)
        print('O valor da raiz quadrada é: %.2f' % squareRoot)
        # print('O valor da raiz quadrada é: %.f' % sqrt(number1))
else:
    print('Nenhum opção válida foi digitada!')