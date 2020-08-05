"""
Escreva um programa que pede os seguintes dados:
• Valor do salário de um funcionário
• Aumento em porcentagem
Depois mostre o valor do aumento e o salário com aumento arredondados para duas
casas decimais
"""
# entrada de dados
salario = float(input("Digite o salario: "))
aumento = float(input("Digite a porcentagem do aumento: "))
# processamento
aumento = salario * (aumento/100)
salario_total = salario + aumento
# saída de dados
# print("O aumento foi de: ", aumento)
print("O aumento foi de %.2f\nTotal é iqual a %.2f" % (aumento, salario_total))