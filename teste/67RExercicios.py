while True:
    n = int(input('Deseja ver a tabuada de qual numero? '))
    if n < 0:
         break
    print('-'*30)
    for c in range(1,11): # rage ignora o ultimo nuemr, entao colocamos um numero a+ de 1 ate 11
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA DA TABUADA ENCERRADO. VOLTE SEMPRE!')
