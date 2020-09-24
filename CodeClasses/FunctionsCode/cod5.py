# Faça um programa que preencha um vetor com 10 elementos numéricos inteiros.
# Calcule e mostre:
# • todos os números pares;
# • a quantidade de números pares;
# • todos os números ímpares;
# • a quantidade de números ímpares.

# 1 criando a função  para peencher uma lista com 10 elementos numéricos
def preenche_vetor(vet, n):
    for i in range(n):
        vet[i] = int(input('Digite o valor indice [%d] = ' % i))

# 2 criando a função par ou impar
def par_ou_impar(vet, vpar, vimpar):
    contPar = 0
    contImpar = 0
    for i in range(len(vet)):
        if (vet[i] % 2 == 0):
            print('Elemento de índice [%d] = %d é Par' % (i, vet[i]))
            contPar += 1
            vpar.append(vet[i])
        else:
            print('Elemento de índice [%d] = %d é Ímpar' % (i, vet[i]))
            contImpar += 1
            vimpar.append(vet[i])
    return contPar, contImpar

# Função Principal
tam = int(input('Digite o tamanho desejado do vetor: '))
vet = [0] * tam
vetPar = []
vetImpar = []
preenche_vetor(vet, tam)
print(vet)
pares, impares = par_ou_impar(vet, vetPar, vetImpar)
print('A quantidade de Pares é %d' % pares)
print('A quantidade de Impares é %d' % impares)
print(vetPar)
print(vetImpar)
