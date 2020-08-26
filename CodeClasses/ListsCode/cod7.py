# Faça um programa que preencha um vetor com cinco números inteiros,
# determine e mostre os números pares e suas respectivas posições
# • Estratégia:
# • 1) Usar um laço para preencher o vetor com os números digitados pelo
# usuário
# • 2) Usar outro laço para percorrer o vetor e para cada elemento do vetor
# verificar se o número é par e se sim, mostrar o elemento e a posição
# dele no vetor

# 0 - tamanho - 1
v = [0] * 5

for i in range(len(v)):
    v[i] = int(input(f'Digite o valor no elemento {i}: '))

for j in range(len(v)):
    if (v[j] % 2 == 0):
        print(f'O valor {v[j]} é par e esta na posição {j}')
        