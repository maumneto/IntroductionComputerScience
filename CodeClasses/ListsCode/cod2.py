# Modifique o programa (notas_lista.py) tal que depois de receber as notas
# dos alunos, calcular a média da turma, e mostrar a posição na lista e a
# nota dos alunos que ficaram de AF (4 <= nota < 7).

notas = [0] * 10
totalNotas = 0

for i in range(len(notas)):
    notas[i] = float(input(f'Digite o valor da nota indice {i}: '))
    totalNotas += notas[i]

media = totalNotas/len(notas)
print(f'A média da turma é {media}')

for j in range(len(notas)):
    if (notas[j] >= 4 and notas[j] < 7):
        print(f'O aluno da posição {j} esta de AF com nota de {notas[j]}')
