def filtragem(*m):
    import numpy as np
    k = np.ravel(m)
    lst = []

    for y in k:
        lst.append(y)

    a = 0
    x = len(lst)
    z = list()
    for n in range(0, x):
        if 0.35 <= lst[a] <= 0.5:
            z.append(lst[a])
        a = a + 1
    print(type(m))
    print(z)




import numpy as np

x = np.array([[0.5, 3, 4, 3], [2, 5, 6, 2], [0.4, 1, 3, 4], [4, 5, 6, 5]])
p = filtragem(x)