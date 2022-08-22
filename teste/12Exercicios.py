preco = float(input('Qual o preco do produto? R$ '))
novoPreco = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novoPreco))