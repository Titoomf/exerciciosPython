n1 = int(input('Digite o primeiro valor: '))
n2= int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novo numeros
    [5] Sair''')
    opcao = int(input('>>>>>>>>>> Qual a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A Soma entre {} e {} é {}'.format(n1, n2 ,soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O Resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior  valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe numero novamente.')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opcao Invalida. Tente novamento!')
    print('-=' * 10)
print('Fim do programa! Volte sempre!')