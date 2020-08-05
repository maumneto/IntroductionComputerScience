"""
Faça um programa que receba duas notas e seus respectivos pesos,
calcule e mostre a média ponderada
"""
# entrada de dados
nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da nota 1 (0 - 1): "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da nota 2 (0 - 1): "))
# processamento
media = nota1*peso1 + nota2*peso2 / (peso1 + peso2)
# saída de dados
print("O valor da sua média é: ", round(media, 2))
