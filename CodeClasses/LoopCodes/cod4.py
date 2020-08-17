while True:
    idade = int(input('Digite a sua idade: '))
    if (idade > 0):
        break
    print('Idade Invalida! Digite novamente!')

print('A idade digitada foi %d' % idade)
