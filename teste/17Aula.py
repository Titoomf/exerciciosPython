'''# estudando sobre lista ( ela é mutavel, entao podemos trocar os elemntos ou adicionar ou mudar de posicao
num = [2, 5, 6 ,9]
num[2] = 2 # aqui eu posso altera os numero , trocar , ( aqui eu troco o 9 por 2, eu pego a posicao 2 , no caso comeca do 0
num.append(7) # o metodo append ele adicionar na ultima posicao
#num.sort() # esse metodo coloca os elementos em ordem
num.sort(reverse=True) # aqui eu posso colocar em ordem de forma do ultimo ao primeir ao contrario
#num.remove(2) # o remove ele procura o primeiro elemento que voce passou como parametro e quando ele acha ele para e exlcui
# se tiver mais elemento com o mesmo parametro dai teremos que usar os laco de repeticao, pois quando ele acha o primeiro ele para

#num.insert(2, 0) # aqui eu consigo inserir um novo elemento colocando na posicao que eu quero, entao na posicao 2 coloca o 0
#num.pop() # pop sem parametros ele deleta o ultimo elemento
#num.pop(2)# pop com paremetro, ele vai na posicao 2 , lembrando que a primeria posicao é o 0, entao na posicao 2 ele vai eliminar

if 2 in num:
  num.remove(2)
else:
    print('Nao encotrei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos') # o len conta quantos elemento tem'''


'''valores = []
valores.append(5)
valores.append(6)
valores.append(8)

for c, v in enumerate(valores):# o enumerate ele mostra a posicao de cada elemnto
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')'''

#------------------Outra forma de alimentar uma lista -------

'''valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor:' ))) # aqui eu vou digitando um valor e adicionadno na lista

for c, v in enumerate(valores):
        print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei no final da lista!')'''

#---------- Outra forma de alimentar uma lista--------------

a = [2, 3, 4, 5,]
b = a[:]# os dois ponto vai fazer uma copia de uma lista de A dentro de B
b[2] = 8 # nesse caso como b ta igual a a ele vai adicionar o 8 nas duas lista se eu passar o : fatiando, ele vai fazer
# uma copia e vai muda so em 1 lista
print(f'lista A: {a}')
print(f'lista B: {b}')