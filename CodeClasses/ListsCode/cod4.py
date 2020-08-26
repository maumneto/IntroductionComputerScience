# Faça um programa que calcule a diferenc¸a entre a soma dos quadrados dos primeiros 100 números naturais e o quadrado da soma. 
# Ex: A soma dos quadrados dos dez primeiros números naturais é, 
# 12 + 22 + ... + 102 = 385 
# O quadrado da soma dos dez primeiros números naturais é, 
# (1 + 2 + ... + 10)2 = 552 = 3025 
# A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma e 3025 - 385 = 2640.

ntermos = 100
somaQuad = 0
quadSoma = 0

for i in range(1, ntermos+1):
    somaQuad = somaQuad + i**2
print(f'Soma dos Quadrados = {somaQuad}')

for j in range(1, ntermos+1):
    quadSoma = quadSoma + j
quadSoma = quadSoma**2
print(f'Quadrado da soma = {quadSoma}')

diff = quadSoma - somaQuad
print(f'O resultado da diferença entre os {ntermos} é = {diff}')
