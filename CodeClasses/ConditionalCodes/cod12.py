# Faça um programa (triang.py) que recebe três valores digitados A, B e C, informando
# se estes podem ser os lados de um triângulo. O ABC é triângulo se A < B + C e B < A
# + C e C < A + B.

a_side = int(input('Digite o lado A: '))
b_side = int(input('Digite o lado B: '))
c_side = int(input('Digite o lado C: '))

# forma 1
if ((a_side < b_side + c_side) and (b_side < a_side + c_side) and (c_side < b_side + a_side)):
    print('É triângulo!')
else:
    print('NÃO é triângulo!')


# forma 2
# if ((a_side < b_side + c_side) and (b_side < a_side + c_side)):
#     if (c_side < b_side + a_side):
#         print('É triângulo!')
#     else:
#         print('NÃO é triângulo!')
# else:
#     print('NÃO é triângulo!')