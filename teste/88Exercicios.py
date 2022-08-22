from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('    JOGO DA MEGA SENA    ')
print('-' * 30)
quant = int (input('Quantos jogos voce quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='* 3, f' SORTEANDO OS {quant} JOGOS ', '-='* 3)
for i, l in enumerate(jogos): # enumerate ele trata o indice e a lista
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5,'<  BOA SORTE!! >', '-='* 5)




