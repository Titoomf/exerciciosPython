'''teste = list()
teste.append('Augusto')
teste.append(28)
galera = list()
galera.append(teste[:]) # os dois ponto é para ele fazer um copiado fatiado, se nao tive ele ia replicar a  lista
teste[0] = 'Gustavo'
teste[1] = 28
galera.append(teste[:])
print(galera)'''

'''galera = [['Joao', 29],['Totti', 30], ['Gabe', 27],['liz', 29]]
# Posicoes:     0             1                 2         3

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''

print('-=' * 30)
galera = list()
dados = list()
totalMaiorIdade = totalMenorIdade = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))#adiciono um nome na lista
    dados.append(int (input('Idade: ')))# adiciono uma idade na lista
    galera.append(dados[:])# aqui eu faço uma copia da lista, lembrado os dois pontos
    dados.clear() # a cada vez que eu faço o laco ele apaga(clear)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        totalMaiorIdade += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        totalMenorIdade += 1
print(f'Temos {totalMaiorIdade} maior de idade e {totalMenorIdade} menores de idade.')
