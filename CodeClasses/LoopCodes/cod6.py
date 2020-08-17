# Escreva um algoritmo para mostrar a tabuada de um número 0 < inteiro
# <=10 entrado pelo usuário usando for

while True:
    num = int(input('Digite o valor o número: '))
    if (num > 0 and num <= 9):
        break
    print('Entrada Inválida! Digite novamente!')

for i in range(1, 11):
    res = num*i
    print('%d x %d = %d' % (num, i, res))
    
print('fim')