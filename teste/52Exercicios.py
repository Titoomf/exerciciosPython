numero = int(input('Digite um numero: '))
tot = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[31m', end=' ')
        tot = tot +1
    else:
        print('\033[35m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[36m O numero {} foi divisivel {} vezes'.format(numero, tot))
if tot == 2:
    print('É Por isso que  é PRIMO!')
else:
    print('É Por isso que  NAO É PRIMO!')