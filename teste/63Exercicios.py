print('-' * 30)
print('Sequencia de Fibonnaci')
print('-' * 30)
n = int(input('Quantos termo voce quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2),end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    cont = cont + 1
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3

print(' -> Fimmm')
