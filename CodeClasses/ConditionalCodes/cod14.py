# Faça um programa que calcule as raízes da equação de 2o grau. Lembre-se que: x = (−b ± √∆)/2a onde ∆ = b2 – 4ac
# E ax2 + bx + c = 0 representa uma equação do 2o grau. A variável ’a’ tem que ser diferente de zero. Caso seja
# igual, imprima a mensagem “Não é equação do segundo grau”.
# Se ∆ < 0, não existe real. Imprima a mensagem “Não existe raiz”.
# Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz Única.
# Se ∆ > 0, imprima as duas raízes.

from math import sqrt

#  entrada de dados
a = float(input('Entre com o valor de a: '))
# validando se é ou não equação do segundo grau! 
if (a == 0):
    print('Não é equação do segundo grau!')
else:
    b = float(input('Entre com o valor de b: '))
    c = float(input('Entre com o valor de c: '))
    #calculo de delta
    delta = b**2 - 4*a*c
    
    # casos do delta
    if ( delta < 0 ):
        print('Não existe raiz real!')
    elif ( delta == 0 ):
        x = (-b + sqrt(delta))/(2*a)
        print('Raiz única cujo o calor é %.2f' % x)
    else:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        print('Raiz 1 = %.2f\nRaiz 2 = %.2f' % (x1, x2))