print('-=' * 20)
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero:'))
print('-=' * 20)
if n1 > n2:
    print('O Primeiro valor é maior')
elif n2 < n1:
    print('O Segundo valor é maior')
elif n1 == n2:
    print('Os dois valores sao iguais')