import math

# codigo aula 3
idade = 29 # tipo inteiro
nota = 7.6 # tipo real
nome = 'Mauricio' # tipo literal
estaVago = True # tipo booleano

print(type(idade))
print(type(nota))
print(type(nome))
print(type(estaVago))

# Este é um comentário de linha!

"""
Comentários 
em 
Multiplas
linhas
"""
'''
Comentários 
em 
Multiplas
linhas
'''
# idade = int(input('Entre com a idade: '))
# print(type(idade))
# nota = float(input('Entre com a nota do aluno: '))
# print(type(nota))

# nome = input('Entre com o seu nome: ')
# print('Olá Sr(a) ',nome)

valor = 4
print(math.sqrt(valor))
pi = 3.1415
print(math.ceil(pi))
print(math.floor(pi))
print(round(pi,2))
# print(dir(math))
help(math.ceil)