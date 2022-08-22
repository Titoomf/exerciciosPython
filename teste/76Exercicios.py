listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo',25,
            'Compasso', 9.99,
            'Mochila', 120.50,
            'Livro', 35.50,
            'Canetas', 22.50,
            'Apontador',5)
print('-='*40)
print(f'{"LISTAGEM DE PRECOS":^40}')
print('-='*40)
for pos in range(0, len(listagem)): # o len pega o tamanho da lista
    if pos % 2 ==0: # os itens estao na posicao par e os preco na impar (0,1)
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-='*40)