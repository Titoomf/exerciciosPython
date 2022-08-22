'''numero = soma = 0
while True:  # aqui ele vai fazer um  loop infinito ate que ele encontre o comando interrompa(break)
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma += numero
#print('A soma vale {}'.format(soma))
print('-'*30)
# uma forma mais facil se printar na tela é com as f strigs
print(f'A Soma vale {soma}')'''''

#EXEMPLO DE F STRINGS
nome = 'José'
idade = 33
salario = 1000
print(f'O {nome} tem {idade} e ganha R${salario:.2f}')