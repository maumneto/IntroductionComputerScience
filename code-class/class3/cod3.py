"""
Faça um programa que receba três notas e calcule e mostre a média
aritmética
"""
# entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
# processamento
media = (nota1 + nota2 + nota3) / 3
# saída de dados
print("O resultado da média é: ", round(media,2))