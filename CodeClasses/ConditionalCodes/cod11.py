i = int(input('Digite sua idade: '))

if (i % 2 == 0):
    i = i + 10
else:
    i = i * 2
    
print('idade final = %d' % i)