from random import randint
x = int(input('\033[01;31mQuantas vezes você quer jogar? '))
z = list()
t = 1
lista = list()
while t <= x:
    for c in range(0, 6):
        n = randint(1, 60)
        z.append(n)
        z.sort()
    lista.append(z[:])
    z.clear()
    t = t+1
print('Os números são: \033[01;35m{}'.format(lista))
