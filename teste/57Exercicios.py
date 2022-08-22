sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0] # vou colocar tudo maiusculo e pegar so a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados Invalidos.Por favor, informe o sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

