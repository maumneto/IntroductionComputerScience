# Faça uma função (cria_matriz) que cria uma matriz m por n, preenchida com zeros e uma função (print_matriz) que mostra uma matriz de qualquer dimensão

# 1. função criar a matriz
def cria_matriz_zeros(m, n):
    mat = []
    for i in range(m):
        linha = [0] * n
        mat.append(linha)
    return mat

# 2. função printar matriz
def print_matriz(m, n, mat):
    for i in range(m):
        for j in range(n):
            print('[%d][%d] = [%d]' % (i+1,j+1,mat[i][j]))

# Programa Principal
linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))
mat = cria_matriz_zeros(linhas, colunas)
print_matriz(linhas, colunas, mat)
