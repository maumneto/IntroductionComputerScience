# Uma pequena loja de artesanato possui apenas um vendedor e comercializa dez tipos de
# objetos. O vendedor recebe, mensalmente, salário de R$545,00, acrescido de 5% do valor
# total de suas vendas. O valor unitário dos objetos deve ser informado e armazenado em um
# vetor; a quantidade vendida de cada peça deve ficar em outro vetor, mas na mesma posição.
# Crie um programa que receba os preços e as quantidades vendidas, armazenando-os em
# seus respectivos vetores (ambos com tamanho dez). Depois determine e mostre:
# • um relatório contendo: a quantidade vendida, valor unitário e valor total de cada objeto.
# Ao final, deverão ser mostrados o valor geral das vendas e o valor da comissão que será
# paga ao vendedor; e
# • o valor do objeto mais vendido e sua posição no vetor (não se preocupe com empates).

tamanho = 5
preco = [0] * tamanho
quantidade = [0] * tamanho
total_vend = 0
total_geral = 0
comissao = 0

for i in range(tamanho):
    preco[i] = float(input(f'Digite o valor do preço unitário indice [{i}]: '))
    quantidade[i] = int(input(f'Digite a quantidade desejada indice [{i}]: '))

for j in range(tamanho):
    total_vend = preco[j] * quantidade[j]
    print(f'Preço {preco[j]} - Quantidade {quantidade[j]} - Total Venda {total_vend}')
    total_geral += total_vend

comissao = total_geral * (5/100)
print(f'O total de vendas é {total_geral} e a comissão é {comissao}')

maior = quantidade[0]
iMaior = 0

for i in range(1,tamanho):
    if (quantidade[i] > maior):
        maior = quantidade[i]
        iMaior = i

print(f'A maior quantidade é {maior} e esta no indice {iMaior}')
