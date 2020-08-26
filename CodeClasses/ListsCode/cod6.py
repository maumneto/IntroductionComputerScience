# Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento de 1.5%. 
# A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. 
# Faça programa que determine o salário atual do funcionário.

percAum = 1.5
salario = 2000
anoAtual = 2020

# 1996
aum = salario * (1.5/100)
totalSal = salario + aum
print(f'Ano: 1996 - Aumento: {aum} - Total Salário: {totalSal}')

for i in range(1997, anoAtual+1):
    percAum = percAum * 2
    aum =  salario * (percAum/100)
    totalSal = salario + aum
    print(f'Ano: {i} - Aumento: {aum} - Total Salário: {totalSal}')