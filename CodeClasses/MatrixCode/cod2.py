mat = []
for i in range(4):
    linha = [0]*4
    mat.append(linha)
print(mat)

mat[2][2] = 8
mat[3][1] = 10
mat[3][3] = 44

print(mat[3][3])

# mat2 = []
# for i in range(4):
#     linhas = []
#     for j in range(3):
#         prof = [0]*3
#         linhas.append(prof)
#     mat2.append(linhas)

# print(mat2)