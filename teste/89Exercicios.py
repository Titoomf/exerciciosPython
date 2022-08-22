ficha = list()
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1,nota2], media])
    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando..')
        break
    if opc <= len(ficha) - 1: # TEM QUE SER MENOR QUE O LEN DE FICHA E NO CASO NO -1 PQ PRIMEIRO ALUNO COMECA EM 0 E O ULTIMO
        # É N -1
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('VOLTE SEMPRE!!!')


