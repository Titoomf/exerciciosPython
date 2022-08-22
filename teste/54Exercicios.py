from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nascimento = int(input('Em que ano a {} pessoa nasceu? '.format(pessoas)))
    idade = atual - nascimento
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmaior + 1
print('Ao todo tivemos {}  pessoas  maiores de idade'.format(totmaior))
print('E tambem tivemos {} pessoas menores de idade '.format(totmenor))


