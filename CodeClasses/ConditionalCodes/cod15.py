value = int(input('Digite um valor de 4 digitos: '))

aux = value

fourth = aux // 1000
aux = aux % 1000

third = aux // 100
aux = aux % 100

second = aux // 10
aux = aux % 10

first = aux // 1

total = first + second + third + fourth

print('O valor do total é %d' % total)
