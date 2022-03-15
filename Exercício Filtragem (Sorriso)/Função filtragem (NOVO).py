import numpy as np


def filtragem(m, lim_min=0.35, lim_max=0.5):
    Vx = np.ravel(m)
    V = list()
    indice = list()
    p = len(m[0])
    for n in range(len(Vx)):
        if lim_min <= Vx[n] <= lim_max:
            V.append(Vx[n])
            indice.append(n)
    valor = np.array((indice)) / p
    v_pos_x = valor.astype(int)
    c = (valor - v_pos_x) * p
    v_pos_y = (np.around(c)).astype(int)
    return V, v_pos_x, v_pos_y


x = np.array([[0.5, 3, 4, 3], [2, 0.458789546498, 6, 2], [0.4, 1, 3, 4], [4, 5, 6, 5]])

a, b, c = filtragem(x)
print(a, b, c)