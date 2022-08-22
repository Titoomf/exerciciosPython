tot = totmil= menor = cont =0
barato = ''
while True:
    produto = str(input('Digite o nome do Produto: '))
    preco = float(input('Digite o preco: R$ '))
    cont += 1
    tot += preco
    if preco >=1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
        ''''' 
        como é igual a outro bloco, posso tirar esse aqui e color o or no bloco acima
    else:
      if preco < menor:
            menor = preco
            barato = produto'''''
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O Total da compra foi R$ {tot:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')