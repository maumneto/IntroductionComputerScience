# Supondo que A, B e C são variáveis de tipo int, com valores iguais a 5, 10 e -8, 
# respectivamente, e uma variável float D, com valor 1.5, 
# quais os resultados das expressões aritméticas a seguir:
# a) 2 * A % 3 - C
# b) ((20 // 3) // 3) + 8**2/2
# criando as variaveis
a = 5
b = 10
c = -8
d = 1.5

res_a = 2 * a % 3 - c
res_b = ((20 // 3) // 3) + 8**2/2

print(res_a)
print(res_b)

# print(a+b != d)
# print(a+b != 15)
# print(a+b == d)
# print(a+b == 15)

# c)3 * 6 == 36/2
# d) 15 % 4 < 19 % 6
# print(3*6 == 36/2)
# print(15%4 == 19%6)

# 2 < 5 and 15/3 == 5
# 1. 2 < 3 and 5 == 5
# 2. True and True
# 3. True
print(2 < 5 and 15/3 == 5)

# False or 20 //(18/3) != (21/3) // 2
print(False or 20 //(18/3) != (21/3) // 2)
