from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O Atleta tem {} anos'.format(idade))
if idade <9:
    print('Classificacao: MIRIM')
elif  idade <=14:
    print('Classificacao: INFANTIL')
elif idade <= 19:
    print('Classificao: Junior')
elif idade <=25:
    print('Clasificacao: Senior')
else:
    print('Clasificacao: Master')