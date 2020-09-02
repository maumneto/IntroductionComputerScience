s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.- '
i = 14
mensagem = s[i] + s[-9] + s[-1] + s[i] + s[-11:-9] + s[24] + s[-9] + s[-1] + s[10] + s[25] + s[-12] + s[i] + s[23] + s[13:15] + s[23] + s[13] + s[24] + s[-1] + s[25] + s[-5] + s[-10] + s[17] + s[24] + s[23] + s[-3]
print(mensagem)