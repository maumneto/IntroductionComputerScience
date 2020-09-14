mat = []
for i in range(3):
    linhas = [0] * 3
    mat.append(linhas)
print(mat)

for i in range(3):
    for j in range(3):
        mat[i][j] = int(input('Digite o valor do indice [%d][%d]: ' % (i, j)))

print(mat)