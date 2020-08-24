# Faça um programa que receba o valor de um empréstimo e mostre uma tabela com os
# seguintes dados: total a pagar, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela à esquerda. Um exemplo de saída
# para um empréstimo de R$1000,00 é mostrado à direita

juros = 10

emp = float(input('Digite o seu emprestimo: '))
juros1 = emp*0.02
valorFinal = emp + juros1
print('Total a Pagar = {} - Valor do Juros = {} - Qtd de Parcelas = 1 - Valor da parcela = {}'.format(round(valorFinal,2),juros1, round(valorFinal,2)))

for i in range(3,13,3): #[3,6,9,12]
    valAcres = emp * (juros/100)
    valorFinal = emp + valAcres
    parc = valorFinal / i
    print('Total a Pagar = {} - Valor do Juros = {} - Qtd de Parcelas = {} - Valor da parcela = {}'.format(round(valorFinal,2),valAcres, i, round(parc,2)))
    juros += 5 #juros = juros + 5