num = (int(input('Digite um numero:')),# montando uma tupla
       int(input('Digite outro numero:')),
       int(input('Digite mais um numero:')),
       int(input('Digite o ultimo numero:')),)
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes ') # contar quantas vezes apareceu o mesmo numero
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posicao ') # index pega a posicao
else:
    print('O valor 3 nao foi digitdo em nenhuma posicao')
print('Os valores pares digitado foram ', end= ' ')
for n in num:
    if n % 2 ==0:
        print(n, end=' ')
