def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        print('Nao ha divisao por zero!')
    else:
        return a/b

def imprimir(a,b,operacao):
    print(operacao(a,b))