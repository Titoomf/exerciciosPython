def area (l, c):
    a = l * c
    print(f'A area de um terreno {l} x {c} é de {a}m2.')

#Programa principal
print('Controle de Terreno')
print('-'*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m)'))
area(l,c)
