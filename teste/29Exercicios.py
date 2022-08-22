velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO!, Voce acabou de ultrapassar o limite de 80km/h')
    multa = (velocidade) * 7
    print('Voce dever pagar uma multa de R${:.2f}'.format(multa))
else:print('Tenha um bom dia! Dirija com segurança!')