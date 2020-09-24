def somar(a,b):
    return a + b

def multiplicar(a,b):
    return a * b

def imprimir(a,b,oper):
    print(oper(a,b))

num1 = int(input('Valor1: '))
num2 = int(input('Valor2: '))

imprimir(num1, num2, somar)