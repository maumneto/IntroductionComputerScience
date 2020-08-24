# Cada espectador de um cinema respondeu a um questionário no qual constava
# sua idade e sua opinião em relação ao filme: ótimo - 3; bom - 2; regular-1.
# Faça um programa que receba a idade e a opinião de 15 espectadores, calcule
# e mostre:
# • A média das idades das pessoas que responderam ótimo;
# • a quantidade de pessoas que responderam regular;
# • e a percentagem de pessoas que responderam bom, entre todos os
# espectadores analisados

from math import floor

totalAge = 0
contOtimo = 0
contReg = 0
contBom = 0

for i in range(15):
    while True:
        opt = int(input('Digite sua opinião\n[1]-Regular\n[2]-Bom\n[3]-Otimo\nResp: '))
        if (opt > 0 and opt < 4):
            break
    
    age = int(input('Digite sua idade: '))

    if (opt == 3):
        totalAge += age
        contOtimo += 1
    elif (opt == 1):
        contReg += 1
    else:
        contBom += 1

mediaPerOtimo = floor(totalAge/contOtimo)

print(f'A média de idade das pessoas que responderam ótimo é {mediaPerOtimo}')
print(f'A quatidade de pessoas que responderam regular é {contReg}')
percentBom = (contBom/15)*100
print('A percentagem das pessoas que responderam bom é {}%'.format(round(percentBom,2)))