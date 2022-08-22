aluno = dict()
aluno['Nome'] = str(input('Digite um nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')