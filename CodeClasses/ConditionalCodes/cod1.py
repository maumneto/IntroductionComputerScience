nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if (media >= 7):
    print("Sua média foi %.2f" % media)
    print("Aprovado!")
else:
    print("Sua média foi %.2f" % media)
    print("Reprovado!")

print("Fim do Algoritmo!")