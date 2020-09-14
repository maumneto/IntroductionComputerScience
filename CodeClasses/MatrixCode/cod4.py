# Faça um programa que preencha uma matriz 2 x 2 e calcule e mostre o seu
# maior elemento

# 1 passo - criar uma matriz (inicialmente de zeros)
mat = []
for i in range(2):
    linha = [0]*2
    mat.append(linha)

# 2 passo - percorrer a matriz adicionando os elementos providos pelo usuario
for i in range(2):
    for j in range(2):
        mat[i][j] = int(input('Digite o valor do indice [%d][%d]: ' % (i, j)))

# 3 passo - achar o maior elemento da minha matriz
major = mat[0][0]
for i in range(2):
    for j in range(2):
        if (major < mat[i][j]):
            major = mat[i][j]
print(f'O maior elemento da matriz é {major}')