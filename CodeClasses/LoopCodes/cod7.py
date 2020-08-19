while True:
    base = float(input('Digite o valor da base: '))
    altura = float(input('Digite o valor da altura: '))
    if ((base > 0) and (altura > 0)):
        break
    else:
        print('Entrada invalida!')
        print('\n')

area = (base*altura)/2

print('A área do triângulo é: ', area)
print('A área do triângulo é: %.2f' % area)
print(f'A área do triângulo é {area}')
print('A área do triângulo é {}'.format(area))