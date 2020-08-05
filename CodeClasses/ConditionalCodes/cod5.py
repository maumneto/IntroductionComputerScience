# Faça um programa para calcular a média aritmética M entre duas notas de
# um aluno e mostrar sua situação, que pode ser aprovado (M ≥ 7),
# reprovado (M < 4) e AF (4 ≤ M < 7). Se o aluno ficar de AF, entre com a
# nota da AF e mostre a média e o resultado final

# entrada de dados
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
# calculo da média
media = (nota1 + nota2) / 2
# estrutura de decisão
if (media >= 7):
    print('O aluno está APROVADO! Vaitimbora!')
    print('Media = %.2f' % media)
elif (media < 4):
    print('O aluno está REPROVADO! Fica mais um pouco!')
    print('Media = %.2f' % media)
else: 
    print('O aluno esta na FINAL! Melhor estudar!')
    print('Media = %.2f' % media)
    nota_final = float(input('Digite a nota final do aluno: '))
    media_final = (nota1 + nota2 + nota_final) / 3
    if (media_final >= 5):
        print('Aprovado na Final!')
        print('Media Final = %.2f' % media_final)
    else: 
        print('Reprovado na Final')
        print('Media Final = %.2f' % media_final)