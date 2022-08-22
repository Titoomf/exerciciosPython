pessoas = {'nome':'Augusto', 'sexo':'M', 'idade': 28}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

'''pessoas['nome'] = 'totii' # posso modificar o nome
pessoas['peso'] = 80 #adiciona mais um elemento sem precisar usar o append
#del pessoas['sexo'] # posso excluir um elemento
for k, v in pessoas.items():
    print(f'{k} = {v}')'''


'''brasil = list()
estado1 = {'uf':'Santa Catarina', 'Sigla': 'SC'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])'''''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str (input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor de {v}.')
