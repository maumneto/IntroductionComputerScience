# Faça um programa que mostre os primeiros 10 termos da sequência de Fibonacci:
# 0-1-1-2-3-5-8-13-21-34-...

a = 0
b = 1

termos = int(input('Digite o número de termos desejados: '))

if (termos <= 0):
    print('Entrada Invalida!')
elif (termos == 1):
    print(f'Termo 1 -> {a}')
elif (termos == 2):
    print(f'Termo 1 -> {a}')
    print(f'Termo 2 -> {b}')
else:
    print(f'Termo 1 -> {a}')
    print(f'Termo 2 -> {b}')
    for i in range(3,termos+1):
        aux = a + b
        print(f'Termo {i} -> {aux}')
        a = b
        b = aux

print('fim!')
