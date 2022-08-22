# Tupla sao imutavies , depois que definiu nao pode mais alterar

times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro','Flamengo', 'Vasco', 'Chapecoense', 'Atletico',
'Atletico-PR','Bahia', 'Sao Paulo', 'Botafogo', 'Fluminense', 'Sport', 'Recife', 'EC Vitoria', 'Coritiba', 'Avai',
'Ponte-Preta', 'Atletico-GO')
print('-='* 30)
print(f'Lista de times do Brasileirão: {times}')
print('-='* 30)

print(f'Os 5 primeiros sao {times[0:5]}')# fatiando para pegar os 5 primeiros times, ele sempre ignora o ultimo elemento
#pois de 0 ate 5 sao 6 times, e ele vai mostra 5
print('-='* 30)

print(f'Os quatros ultimos times sao  {times[-4:]}')#mostra os 4 ultimos times
print('-='* 30)
print(f'Times em ordem alfabetica: {sorted(times)}')# sorted ele coloca em ordem alfabetica
print('-='* 30)
print(f'O Vasco esta na {times.index("Vasco")+1}  posicao ')



'''Outra solucao
for t in times:
    print(t)'''

