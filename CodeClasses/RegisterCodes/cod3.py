# Faça um programa em Python para criar um estoque de produtos. Cada produto possui
# um código, um preço e uma quantidade. O estoque pode armazenar 10 produtos.
# Depois de receber os produtos do estoque, mostre um relatório com os produtos, a
# quantidade total de itens e o valor total do estoque.

# Use uma função cria_produto para criar um registro com código, preço e quantidade
# e outra função que mostra_produto para mostrar os valores dos campos de um
# produto

# função criar produto e adicionar ao estoque
def cria_produto(estoque, num=1):
    for i in range(2):
        produto = {}
        produto['nome'] = input('Nome #%d: ' % i)
        produto['codigo'] = int(input('Código #%d: ' % i))
        produto['preco'] = float(input('Preço #%d: ' % i))
        produto['quantidade'] = int(input('Quantidade #%d: ' % i))
        estoque_prod.append(produto)
        print('Produto #%d adicionado ao estoque' % produto['codigo'])
        print('')

# mostrar relatorio do produto
def mostrar_relatorio(estoque):
    quantidade_total = 0
    valor_total = 0
    for i in range(len(estoque)):
        print('Produto #%d' % i)
        print('Nome do Produto = %s' % estoque[i]['nome'])
        print('Código do Produto = %d' % estoque[i]['codigo'])
        print('Preço do Produto = %.2f' % estoque[i]['preco'])
        print('Qtd do Produto = %d' % estoque[i]['quantidade'])
        print('')
        quantidade_total = quantidade_total + estoque[i]['quantidade']
        valor_total += (estoque[i]['preco'] * estoque[i]['quantidade'])
    
    print('A quantidade total de produtos = %d' % quantidade_total)
    print('O valor total do estoque = %.2f' % valor_total)

# 1. criar o estoque de produtos
print('Bem vindo ao estoque de produtos!')
estoque_prod = []
n = int(input('Entre com o total de produtos a serem add:  '))
# 2. receber os produtos do estoque
cria_produto(estoque=estoque_prod, num=n)
# 3. mostrar o relatório
mostrar_relatorio(estoque_prod)