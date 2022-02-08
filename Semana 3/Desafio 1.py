def voto(a):
    if 0 <= a < 16:
        print('Voto negado !!!')
    elif a < 0:
        print(f'Viajante do tempo detectado !')
    elif 16 < a < 18 or a > 60:
        print('Voto facultativo')
    else:
        print('voto obrigatório')

    return(a)


a = int(input('Insira a sua idade: '))
voto(a)





