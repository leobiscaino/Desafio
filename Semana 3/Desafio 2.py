def maior(*num):
    x = len(num)
    z = 0
    a = -1
    y = a+1
    for n in range(0, x-1):
        a = a + 1
        if num[a] >= num[y]:
            z = num[a]
    print(f'O maior valor é: \033[01;32m{z}')


maior(14, 14, 13)

