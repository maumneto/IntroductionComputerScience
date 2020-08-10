# Um programa para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para
# decidir o número de notas de cada valor que deve ser disponibilizado para o cliente que realizou o
# saque. Um possível critério seria o da “distribuição ótima” no sentido de que as notas de menor valor
# sejam distribuídas em número mínimo possível.
# Escreva um programa que leia o valor da quantia solicitada e imprima na tela a distribuição das notas
# de acordo com o critério acima. Considere apenas a existência das notas de R$50, R$10, R$5 e R$1
# no caixa eletrônico.
# Exemplo: Ao digitar R$87, a impressão deve mostrar:
# Nota50 = 1
# Nota10 = 3
# Nota5 = 1
# Nota1 = 2

#  entrada de dados
cash = int(input('Digite a quantia desejada: '))

# atribuindo o conteúdo de cash a variável aux
aux = cash

#  calculo da nota de 50 reais
cash50 = aux // 50
aux = aux % 50 # atualizando o valor de auxiliar

#  calculo da nota de 10 reais
cash10 = aux // 10
aux = aux % 10 # atualizando o valor de auxiliar

#  calculo da nota de 5 reais
cash5 = aux // 5
aux = aux % 5 # atualizando o valor de auxiliar

#  calculo da nota de 1 reais
cash1 = aux // 1

print('Valor Requerido: %d' % cash)
print('Nota de R$ 50: %d\nNota de R$ 10: %d\nNota de R$ 5: %d\nNota de R$ 1: %d' % (cash50, cash10, cash5, cash1))