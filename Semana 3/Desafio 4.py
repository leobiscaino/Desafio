def fac(num=1):
    f = 1
    for c in range(num, 0, -1):
        f = f*c
    return(f)


x = int(input('Quantos fatoriais quer calcular ? '))
lista = list()
for c in range(0, x):
    n = int(input('Digite o fatorial desejado: '))
    fac(n)
    lista.append(fac(n))
print(f' Os valores obtidos são: {lista} ')