peso = float(input('Qual seu peso? (kg)'))
altura = float(input('Qual sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO normal')
elif imc >= 18.5 and imc <25:
    print('PARABENS,voce esta na faixa de PESO NORMAL')
elif 25 <= imc <= 30:
    print('Voce esta com SOBREPESO')
elif 30 <= imc <=40:
    print('voce esta na,OBESIDADE, cuidado!')
elif imc >= 40:
    print('Voce esta em OBESIDADE MORBIDA, cuidado!')

