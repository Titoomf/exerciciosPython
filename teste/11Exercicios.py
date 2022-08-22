largura = float(input('Digite uma largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print(f'Sua parede tem a dimensao de {largura}x{altura} e sua area é de {area}m²')
tinta = area / 2
print('Para pintar essa parede, voce precisara de {}l de tinta.'.format(tinta))