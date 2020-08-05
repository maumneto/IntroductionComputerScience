# Escreva um programa (salario.py) que pede os seguintes dados:
# Valor do salário de um funcionário
# Aumento em porcentagem
# Depois mostre o valor do aumento e o salário com aumento com duas casas decimais

salario = float(input('Digite o valor do salário: '))
porc_aumento = float(input('Entre com o aumento: '))

aumento = salario * (porc_aumento/100)
salario_total = salario + aumento

print('O aumento foi de %.2f\nSalário Total = %.2f' % (aumento, salario_total))