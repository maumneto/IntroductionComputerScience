text = input('Escreva algo: ')
subtext = input('string de busca: ')

text = text.lower()
subtext = subtext.lower()
i = 0

while (i > -1):
    i = text.find(subtext, i)
    if (i >= 0):
        print('Encontrado na posição %d' % i)
        i += 1

