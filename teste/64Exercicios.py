numero = cont = soma = 0
numero = int(input('Digite um numero [10 para parar]: ')) # aqui eu nao quero que ele leia o 999 como numeor e sim para parar
while numero !=10:
    soma = soma + numero
    cont = cont + 1
    numero = int(input('Digite um numero [10 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))
