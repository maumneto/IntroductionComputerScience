"""
Faça um programa que receba um número positivo e maior que zero, calcule
e mostre:
• a) o número digitado ao quadrado
• b) o número digitado ao cubo
• c) a raiz quadrada do número digitado
• d) a raiz cúbica do número digitado
"""
from math import sqrt
# import math as m

#entrada de dado
num = int(input("Digite um valor inteiro e positivo: "))
#processamento
quadrado = pow(num, 2)
cubo = num**3
raiz_quad = sqrt(num)
raiz_cub = num**(1/3)
#saída de dados
print("O quadrado do número: ", quadrado)
print("O cubo do número: ", cubo)
print("A raiz quadrada do número: ", round(raiz_quad,2))
print("A raiz cúbica do número: ", round(raiz_cub,2))