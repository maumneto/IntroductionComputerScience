salario = float(input('Digite o valor do salario: '))
perc = float(input('Digite o valor do percentual de aumento: '))

aumento = lambda sal, p : (sal * p/100)

print('O valor do aumento eh: ', aumento(salario, perc))
