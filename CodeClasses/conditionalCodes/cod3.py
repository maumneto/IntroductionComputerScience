# entrada de dados!
nota1 = float(input("Trabalho de laboratório: "))
nota2 = float(input("Avaliação semestral: "))
nota3 = float(input("Exame Final: "))

# calculo da média
media = (nota1 * 0.2 + nota2 * 0.3 + nota3 * 0.5)/(0.2 + 0.3 + 0.5)
print("Sua média é igual a: %.2f" % media)

if (media < 5):
    print("conceito E")
elif (media >= 5 and media < 6):
    print("conceito D")
elif (media >= 6 and media < 7):
    print("conceito C")
elif (media >= 7 and media < 8):
    print("conceito B")
else:
    print("conceito A")

print("fim de algoritmo!")
