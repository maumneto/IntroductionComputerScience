"""
Faça um programa que calcule e mostre a área de um círculo. Sabe-se que
área = π * R²
"""
# entrada de dados
pi = 3.1415
raio = float(input("Digite o raio: "))
# processamento
area_circulo = pi * (raio**2)
# saída de dados
print("O área do círculo é: ", round(area_circulo, 2))