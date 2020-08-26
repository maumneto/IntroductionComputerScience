# Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
# adição (opção 1)
# subtração (opção 2)
# multiplicação (opção 3)
# divisão (opção 4)
# sa´ıda (opção 5)
# O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. O programa são termina quando for escolhida a opção de saída (opção 5).


while True:
    print('')
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    opt = int(input('Digite a opção:\n[1] - Adição\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Saída\nResp: '))

    if (opt == 1):
        res = num1 + num2
        print(f'O resultado da soma é: {res}')
    elif (opt == 2):
        res = num1 - num2
        print(f'O resultado da subtração é: {res}')
    elif (opt == 3):
        res = num1 * num2
        print(f'O resultado da multiplicação é: {res}')
    elif (opt == 4):
        if (num2 == 0):
            print('Não é possível divisão por zero!')
        else:
            res = num1 / num2
            print(f'O resultado da divisão é: {res}')
    elif (opt == 5):
        print('Fim de Execução!')
        break
    else:
        print('Não foi escolhido nenhuma opção valida!')
