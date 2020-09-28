funcionarios = []

for i in range(2):
    funcionario = {}
    funcionario['nome'] = input('Digite o seu nome: ')
    funcionario['cpf'] = int(input('Digite seu CPF: '))
    funcionarios.append(funcionario)
    print('Funcionario %d adicionado com sucesso!\n' % i)

for i in range(len(funcionarios)):
    print('Dados do Funcionário %d' % i)
    print(funcionarios[i]['nome'])
    print(funcionarios[i]['cpf'])