def somar(*args):
    res = 0
    for i in args:
        res += i # equivale a -> res = res + i
    return res

print(somar(1))
print(somar(1,2))
print(somar(1,2,3))
print(somar(1,2,3,4))