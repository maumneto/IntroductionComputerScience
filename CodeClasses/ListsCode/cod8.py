v = [0] * 5

for i in range(len(v)):
    v[i] = int(input(f'Digite o valor indice {i}: '))

for i in range(len(v)):
    cont = 0
    for j in range(1, v[i]+1):
        if (v[i] % j ==  0):
            cont += 1
    if (cont == 2):
        print(f'O valor {v[i]} é primo e esta no indice {i}')
      
    