num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
      [1] Converte para BINARIO
      [2] Converte para OCTAL
      [3] Converte para HEXADECIMAL''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{} Convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para HEXDECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opcao invalida,Tente novamento!')
