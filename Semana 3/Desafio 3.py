def printint(w):
    if type(w) == int:
        print(f'\033[01;31mo número escolhido é:\033[m \033[04;32m{w}')
    else:
        while True:
          if type(w) != int:
              try:
                w = int(input("Digite um número inteiro: "))
                break
              except ValueError:
                  print("\033[01;31;40mApenas numeros inteiros !!\033[m")
                  continue
        print(f'\033[01;31mo número escolhido é:\033[m \033[04;32m{w}')


x=printint('21')
