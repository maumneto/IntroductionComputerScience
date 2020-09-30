def fatorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * fatorial(num-1)

n = int(input('Digite o valor do fatorial: '))
res = fatorial(n)
print(f'O valor do fatorial de {n} é {res}')