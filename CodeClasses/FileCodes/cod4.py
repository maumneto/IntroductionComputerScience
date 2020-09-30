# abrindo o arquivo em modo de escrita!!
file_write = open('numeros.txt', 'w')

for i in range(1,101):
    file_write.write('%d\n' % i)

file_write.close()


# abrindo o arquivo em modo de leitura!!
file_read = open('numeros.txt', 'r')

for i in file_read.readlines():
    print(i)

file_read.close()
print('fim!')