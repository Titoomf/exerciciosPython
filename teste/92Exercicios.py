from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['Contratacao'] = int(input('Ano de Contratação: '))
    dados['Salario'] = float(input('Salario R$'))
    dados['Aposentadoria'] = dados['idade']+(dados['Contratacao'] + 35) - datetime.now().year
print('-=' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')

print(dados)
