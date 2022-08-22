temporario = []
principal= []
maior = menor = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resposta = str(input('Deseja Continuar? [S/N]'))
    if resposta in 'Nn':
        break
print('-=' * 40)
print(f'Os dados foram {principal}')
print(f'Ao todo, voce cadastrou {len(principal)} pessoas')
print(f'O maior peso foi  de {maior}Kg peso de ', end=' ')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}kg. peso de ',end= ' ')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]',end=' ')
print()
