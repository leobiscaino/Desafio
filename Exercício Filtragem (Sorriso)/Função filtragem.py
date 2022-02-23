def filtragem(*m):
    a = 0
    x = len(m)
    z = list()
    for n in range(0, x):
        if 0.35 <= m[a] <= 0.5:
            z.append(m[a])
        a = a + 1
    print(type(m))
    print(z)


lista = filtragem(0.35, 12, 0.5, 54, 0.4)