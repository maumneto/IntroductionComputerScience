# Faça um programa que preencha um vetor com 10 elementos numéricos inteiros.
# Calcule e mostre:
# • todos os números pares;
# • a quantidade de números pares;
# • todos os números ímpares;
# • a quantidade de números ímpares.

vet = [0] * 10
contPar = 0
contImpar = 0

for i in range(len(vet)):
    vet[i] = int(input(f'Digite o valor do indice [{i}]: '))

for j in range(len(vet)):
    if (vet[j] % 2 == 0):
        print(f'O elemento indice [{j}] cujo valor é {vet[j]} é par')
        contPar += 1
    else:
        print(f'O elemento indice [{j}] cujo valor é {vet[j]} é ímpar')
        contImpar += 1

print(f'A quantidade de pares é {contPar}')
print(f'A quantidade de ímpares é {contImpar}')