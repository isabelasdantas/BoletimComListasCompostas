ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('*' * 15)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('*' * 15)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('--' * 30)
    aluno = int(input('Mostrar nota de qual aluno: (999 para finalizar): '))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    if aluno <= len(ficha) - 1:
        print(f'Notas de {ficha[aluno][0]} são {ficha[aluno][1]}')
print('<<<< VOLTE SEMPRE >>>>')
