import calcOper as co

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

co.imprimir(num1, num2, co.somar)
co.imprimir(num1, num2, co.subtrair)
co.imprimir(num1, num2, co.dividir)
co.imprimir(num1, num2, co.multiplicar)