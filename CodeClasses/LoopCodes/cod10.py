# Faça um programa que receba um número inteiro maior que 1, verifique se o
# número fornecido é primo ou não e mostre uma mensagem de número primo ou
# de número não primo. Um número é primo quando é divisível apenas por 1 e
# por ele mesmo.

# Faça um programa que receba dez números inteiros e mostre a quantidade de
# números primos dentre os números que foram digitados.

contadorPrimo = 0
contador = 0

for j in range(10):
    num = int(input(f'Digite um valor inteiro acima de 1 [{j}]: '))
    if (num <= 1):
        print('Entrada Invalida!')
        break
    
    for i in range(2, num):
        if (num % i == 0):
            contador += 1 # contador = contador + 1
        
    if (contador == 0):
        print('É primo!')
        contadorPrimo += 1
    else:
        print('Não é primo!')

print(f'Total de Números Primos: {contadorPrimo}')
print('fim!')