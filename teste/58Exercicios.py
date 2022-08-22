from random import randint
computador = randint(0, 100)
print('Olá,Sou o seu computador... Acabei de pensar em um numero entre 0 e 10 ')
print('Será que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador =int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('MENOS... Tente mais uma vez')
print('Acertou com {} Tentativas, acertouuu Miseraviiiiiiii'.format(palpites))
