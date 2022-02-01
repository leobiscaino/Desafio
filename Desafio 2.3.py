aluno = dict()
aluno['nome'] = str(input('Insira o seu nome: '))
aluno['media'] = float(input('Insira sua média: '))
if aluno['media'] < 6:
    aluno['situacao'] = 'Reprovado'
    print(f'O aluno {aluno["nome"]} está \033[01;31m {aluno["situacao"]}\033[m')
else:
    aluno['situacao'] = 'Aprovado'
    print(f'O aluno {aluno["nome"]} está \033[01;32m{aluno["situacao"]}\033[m. Parabéns ! ')
