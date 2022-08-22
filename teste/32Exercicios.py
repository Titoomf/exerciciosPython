from datetime import datetime
ano = int(input('Que ano quer analisar? '))
if ano ==0:
    ano = datetime.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:

    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('o ano {} Não É BISSEXTO'.format(ano))