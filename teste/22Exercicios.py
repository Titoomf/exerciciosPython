nome = str(input('Digite o seu nome Completo: ')).strip() #corta as espacos antes e depois o que sobraram
print('Analisando seu nome ....')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #Aqui ele vai conta quantos espaco tem e eliminar(todos)
#print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # find encontrara o primeiro espaco o que vier antes é o nome


#aqui ele separa o nomes em lista e depois pega a posicao.
separa = nome.split()
print('Seu primero nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))