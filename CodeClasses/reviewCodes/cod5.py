peso = float(input('Entre com o seu peso: '))
altura = float(input('Entre com a sua altura: '))
imc = peso / (altura**2) # ou peso / (altura * altura)
print('Seu IMC é: ',imc)