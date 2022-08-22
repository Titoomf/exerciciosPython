primeiro = int(input('Primeiro termno: '))
razao = int(input('Razao: '))
decimo = primeiro + (11 - 1) * razao
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end=' ')
print('Acabouuu!!! ')