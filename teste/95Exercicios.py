time = list()
jogador = dict()
partidas  =list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partidas {c + 1} ?')))
    jogador['gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        respos = str(input('Deseja continuar? [S/N]')).upper()[0]
        if respos in 'SN':
            break
        print('ERRO, RESPONDA APENAS S OU N.')
    if respos == 'N':
        break
print('-='* 30)
print('Codigo', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='* 30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para Parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro, NAO EXISTE JOGADOR COM O CODIGO {busca}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGDOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   no jogo {i + 1} fez {g} golls')
    print('-=' * 30)
print('VOLTE SEMPRE ;)')




