def somar(a,b):
    return a + b


def criar_cadastro():
    name = input('Digite o seu nome: ')
    age = int(input('Digite sua idade: '))
    return name, age

nome, idade = criar_cadastro()
print(f'Olá sr(a) {nome}. Você tem {idade} anos!')