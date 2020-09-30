# abrir um arquivo em modo de escrita para inserir valores pares
file_even = open('even_values.txt', 'w')

for i in range(1, 1001):
    if i % 2 == 0:
        file_even.write('%d\n' % i)

file_even.close()

# abrir um arquivo em modo de escrita para inserir valores impares
file_odds = open('odd_values.txt', 'w')

for i in range(1, 1001):
    if i % 2 != 0:
        file_odds.write('%d\n' % i)

file_even.close()
