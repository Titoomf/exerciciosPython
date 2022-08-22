print('{:=^40}'.format(' LOJAS CANTO FELIX '))
preco = float(input('Preco das compras: '))
print(''' FORMA DE PAGAMENTO
[1] a vista dinheiro/cheque
[2] a vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
opcao = int(input('Qual é a opcao? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua conta sera parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalParcelar = int(input('Quantas parcelas ?'))
    parcela = total / totalParcelar
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totalParcelar, parcela))
else:
    total = preco
    print('OPCAO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
