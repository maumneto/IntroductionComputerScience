def barra(caractere='-', qtd=20):
    print(caractere * qtd)

def validar_entrada(pergunta, max, min):
    while True:
        valor = int(input(pergunta))
        if (valor <= min or valor >= max):
            print('Entrada Inválida! Digite um valor entre %d e %d' % (max, min))
        else:
            print('Entrada correta!')
            return valor


# função principal
# perg = 'Qual o valor de entrada: '
# max = int(input('Valor maximo: '))
# min = int(input('Valor minimo: '))
# validar_entrada(perg, max, min)

barra()
barra('*')
barra('*', 50)